from aws_cdk import (
    Stack, CfnParameter, Duration, Aws,
    aws_codepipeline as codepipeline,
    aws_codepipeline_actions as actions,
    aws_codebuild as codebuild,
    aws_iam as iam,
    aws_sns as sns,
    aws_events as events,
    aws_events_targets as targets,
)
from constructs import Construct


class PipelineStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # ----- Parameters -----
        conn_arn = CfnParameter(self, "GitHubConnectionArn", type="String")
        repo_owner = CfnParameter(self, "RepoOwner", type="String")
        repo_name  = CfnParameter(self, "RepoName",  type="String", default="ai-agents-portfolio")
        branch     = CfnParameter(self, "Branch",    type="String", default="main")
        image_repo = CfnParameter(self, "EcrRepoName", type="String", default="ai-agents-portfolio")

        # ----- Artifacts -----
        source_out = codepipeline.Artifact()
        build_out  = codepipeline.Artifact()

        # ----- Source (CodeConnections GitHub) -----
        source = actions.CodeStarConnectionsSourceAction(
            action_name="GitHub",
            owner=repo_owner.value_as_string,
            repo=repo_name.value_as_string,
            branch=branch.value_as_string,
            connection_arn=conn_arn.value_as_string,
            output=source_out,
            code_build_clone_output=True,
            trigger_on_push=True,
        )

        # ----- Use a single IAM role for CodeBuild (mutable so CDK can add inline policy) -----
        cb_role = iam.Role.from_role_arn(
            self, "AiAgentsRole",
            f"arn:aws:iam::{Aws.ACCOUNT_ID}:role/ai-agents",
            mutable=True,
        )
        # Allow this role to PassRole itself to App Runner (image builder + service)
        cb_role.add_to_principal_policy(iam.PolicyStatement(
            actions=["iam:PassRole"],
            resources=[f"arn:aws:iam::{Aws.ACCOUNT_ID}:role/ai-agents"],
            conditions={"StringEquals": {"iam:PassedToService": [
                "apprunner.amazonaws.com", "build.apprunner.amazonaws.com"
            ]}},
        ))

        # ----- Build (docker build + push; emits image.json) -----
        build_project = codebuild.PipelineProject(
            self, "Build",
            role=cb_role,
            environment=codebuild.BuildEnvironment(privileged=True),
            build_spec=codebuild.BuildSpec.from_source_filename("buildspec.yml"),
        )
        # Minimal extras needed by buildspec
        build_project.add_to_role_policy(iam.PolicyStatement(
            actions=["ecr:*", "sts:GetCallerIdentity"],
            resources=["*"],
        ))

        build = actions.CodeBuildAction(
            action_name="BuildAndPush",
            input=source_out,
            outputs=[build_out],
            project=build_project,
            environment_variables={
                # optional: let Build know the ECR repo name from parameter
                "IMAGE_REPO": codebuild.BuildEnvironmentVariable(value=image_repo.value_as_string)
            }
        )

        # ----- Deploy (App Runner create/update from ECR image) -----
        deploy_project = codebuild.PipelineProject(
            self, "Deploy",
            role=cb_role,
            environment=codebuild.BuildEnvironment(privileged=False),
            build_spec=codebuild.BuildSpec.from_object({
                "version": "0.2",
                "phases": {
                    "build": {
                        "commands": [
                            'aws sts get-caller-identity --query Arn --output text',
                            'echo "ACCESS_ROLE_ARN=${ACCESS_ROLE_ARN}"',
                            'set -eu',
                            # read image.json produced by Build
                            'IMAGE=$(python -c "import json; print(json.load(open(\'image.json\'))[\'imageUri\'])")',
                            # get existing service arn if any
                            'SVC=$(aws apprunner list-services --query "ServiceSummaryList[?ServiceName==\'ai-agents-portfolio\'].ServiceArn" --output text)',
                            # ensure App Runner SLR exists (first use only)
                            'aws iam create-service-linked-role --aws-service-name apprunner.amazonaws.com || true',
                            # resolve default access role if not provided by action env var
                            'ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)',
                            'ACCESS_ROLE_ARN="${ACCESS_ROLE_ARN:-arn:aws:iam::${ACCOUNT_ID}:role/ai-agents}"',
                            # build SourceConfiguration JSON safely
                            'SRC_CONFIG=$(python -c "import json,os; '
                            'print(json.dumps({'
                            '\'ImageRepository\':{\'ImageIdentifier\': os.environ[\'IMAGE\'], '
                            '\'ImageRepositoryType\':\'ECR\', '
                            '\'ImageConfiguration\':{\'Port\':\'8080\'}}, '
                            '\'AuthenticationConfiguration\':{\'AccessRoleArn\': os.environ[\'ACCESS_ROLE_ARN\']}, '
                            '\'AutoDeploymentsEnabled\': True}))")',
                            # create or update
                            'if [ -z "$SVC" ]; then '
                            '  aws apprunner create-service --service-name ai-agents-portfolio '
                            '    --source-configuration "$SRC_CONFIG"; '
                            'else '
                            '  aws apprunner update-service --service-arn "$SVC" '
                            '    --source-configuration "$SRC_CONFIG"; '
                            'fi',
                            # output service url
                            'aws apprunner describe-service --service-arn $(aws apprunner list-services '
                            '  --query "ServiceSummaryList[?ServiceName==\'ai-agents-portfolio\'].ServiceArn" '
                            '  --output text) --query Service.ServiceUrl --output text'
                        ]
                    }
                },
                "artifacts": {"files": ["image.json"]}
            }),
            timeout=Duration.minutes(15),
        )

        deploy = actions.CodeBuildAction(
            action_name="Deploy",
            input=build_out,
            project=deploy_project,
            environment_variables={
                # pass the ECR access role explicitly
                "ACCESS_ROLE_ARN": codebuild.BuildEnvironmentVariable(
                    value=f"arn:aws:iam::{Aws.ACCOUNT_ID}:role/ai-agents"
                )
            }
        )

        # ----- Pipeline -----
        pipeline = codepipeline.Pipeline(
            self, "AiAgentsPortfolio",
            stages=[
                codepipeline.StageProps(stage_name="Source", actions=[source]),
                codepipeline.StageProps(stage_name="Build",  actions=[build]),
                codepipeline.StageProps(stage_name="Deploy", actions=[deploy]),
            ],
        )

        # ----- Notifications (EventBridge -> SNS) -----
        topic = sns.Topic(self, "PipelineTopic")
        events.Rule(
            self, "PipelineEventRule",
            event_pattern=events.EventPattern(
                source=["aws.codepipeline"],
                detail_type=[
                    "CodePipeline Pipeline Execution State Change",
                    "CodePipeline Action Execution State Change",
                ],
                detail={"pipeline": [pipeline.pipeline_name]},
            ),
            targets=[targets.SnsTopic(topic)],
        )
