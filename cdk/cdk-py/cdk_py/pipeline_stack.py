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

        # Parameters
        conn_arn = CfnParameter(self, "GitHubConnectionArn", type="String")
        repo_owner = CfnParameter(self, "RepoOwner", type="String")
        repo_name = CfnParameter(self, "RepoName", type="String", default="ai-agents-portfolio")
        branch = CfnParameter(self, "Branch", type="String", default="main")
        image_repo = CfnParameter(self, "EcrRepoName", type="String", default="ai-agents-portfolio")

        # Artifacts
        source_out = codepipeline.Artifact()
        build_out = codepipeline.Artifact()

        # Source
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

        cb_role = iam.Role.from_role_arn(self, "AiAgentsRole",
                                         f"arn:aws:iam::{Aws.ACCOUNT_ID}:role/ai-agents", mutable=False)

        # Build (docker build + push; outputs image.json)
        build_project = codebuild.PipelineProject(
            self, "Build",
            role=cb_role, 
            environment=codebuild.BuildEnvironment(privileged=True),
            build_spec=codebuild.BuildSpec.from_source_filename("buildspec.yml"),
        )
        build_project.add_to_role_policy(iam.PolicyStatement(
            actions=["ecr:*", "sts:GetCallerIdentity"],
            resources=["*"]
        ))

        build = actions.CodeBuildAction(
            action_name="BuildAndPush",
            input=source_out,
            outputs=[build_out],
            project=build_project
        )

        deploy_project = codebuild.PipelineProject(
            self, "Deploy",
            role=cb_role, 
            environment=codebuild.BuildEnvironment(privileged=False),
            build_spec=codebuild.BuildSpec.from_object({
                "version": "0.2",
                "phases": {
                    "build": {"commands": [
                        # POSIX-sh safe one-liners (no heredocs)
                        'set -eu',
                        'IMAGE=$(python -c "import json; print(json.load(open(\'image.json\'))[\'imageUri\'])")',
                        'aws sts get-caller-identity',
                        'echo "ACCESS_ROLE_ARN=$ACCESS_ROLE_ARN"',
                        'SVC=$(aws apprunner list-services --query "ServiceSummaryList[?ServiceName==\'ai-agents-portfolio\'].ServiceArn" --output text)',
                        'aws iam create-service-linked-role --aws-service-name apprunner.amazonaws.com || true',
                        'ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)',
                        'ACCESS_ROLE_ARN="${ACCESS_ROLE_ARN:-arn:aws:iam::${ACCOUNT_ID}:role/ai-agents}"',
                        'SRC_CONFIG=$(python -c "import json,os; print(json.dumps({\'ImageRepository\':{\'ImageIdentifier\': os.environ[\'IMAGE\'], \'ImageRepositoryType\':\'ECR\', \'ImageConfiguration\':{\'Port\':\'8080\'}}, \'AuthenticationConfiguration\':{\'AccessRoleArn\': os.environ[\'ACCESS_ROLE_ARN\']}, \'AutoDeploymentsEnabled\': True}))")',
                        'if [ -z "$SVC" ]; then aws apprunner create-service --service-name ai-agents-portfolio --source-configuration "$SRC_CONFIG"; else aws apprunner update-service --service-arn "$SVC" --source-configuration "$SRC_CONFIG"; fi',
                        'aws apprunner describe-service --service-arn $(aws apprunner list-services --query "ServiceSummaryList[?ServiceName==\'ai-agents-portfolio\'].ServiceArn" --output text) --query Service.ServiceUrl --output text'
                    ]}
                },
                "artifacts": {"files": ["image.json"]}
            }),
            timeout=Duration.minutes(15),
        )

        # Permissions for Deploy project
        # deploy_project.role.add_to_policy(iam.PolicyStatement(
        #     actions=["iam:PassRole"],
        #     resources=[f"arn:aws:iam::{Aws.ACCOUNT_ID}:role/ai-agents"],
        #     conditions={"StringEquals": {
        #         "iam:PassedToService": ["apprunner.amazonaws.com", "build.apprunner.amazonaws.com"]
        #     }},
        # ))

        # deploy_project.add_to_role_policy(iam.PolicyStatement(
        #     actions=[
        #         "apprunner:CreateService", "apprunner:UpdateService",
        #         "apprunner:DescribeService", "apprunner:ListServices"
        #     ],
        #     resources=["*"]
        # ))

        # deploy_project.add_to_role_policy(iam.PolicyStatement(
        #     actions=["iam:CreateServiceLinkedRole"],
        #     resources=["*"],
        #     conditions={"StringEquals": {"iam:AWSServiceName": "apprunner.amazonaws.com"}}
        # ))
        # # Ensure SLR exists (no-op if already present)
        # iam.CfnServiceLinkedRole(self, "AppRunnerSLR", aws_service_name="apprunner.amazonaws.com")

        # Allow passing the ECR access role to App Runner (defaults to role/ai-agents)
        # if deploy_project.role is not None:
        #     deploy_project.role.add_to_policy(iam.PolicyStatement(
        #         actions=["iam:PassRole"],
        #         resources=[f"arn:aws:iam::{Aws.ACCOUNT_ID}:role/ai-agents"],
        #         conditions={"StringEquals": {"iam:PassedToService": "apprunner.amazonaws.com"}}
        #     ))

        deploy = actions.CodeBuildAction(
            action_name="Deploy",
            input=build_out,
            project=deploy_project,
            environment_variables={
                "ACCESS_ROLE_ARN": codebuild.BuildEnvironmentVariable(
                    value=f"arn:aws:iam::{Aws.ACCOUNT_ID}:role/ai-agents"
                )
            }
        )

        pipeline = codepipeline.Pipeline(
            self, "AiAgentsPortfolio",
            stages=[
                codepipeline.StageProps(stage_name="Source", actions=[source]),
                codepipeline.StageProps(stage_name="Build", actions=[build]),
                codepipeline.StageProps(stage_name="Deploy", actions=[deploy]),
            ]
        )

        # Notifications via EventBridge -> SNS
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
