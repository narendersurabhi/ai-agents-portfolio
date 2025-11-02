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
        # ----- IAM Roles -----
        # role for App Runner to access ECR images  
        ecr_access_role = iam.Role(
            self, "AppRunnerEcrAccessRole",
            assumed_by=iam.ServicePrincipal("build.apprunner.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "service-role/AWSAppRunnerServicePolicyForECRAccess"
                )
            ],
        )
        # role for CodeBuild projects in pipeline   
        codebuild_role = iam.Role(
            self, "CodeBuildPipelineRole",
            assumed_by=iam.ServicePrincipal("codebuild.amazonaws.com"),
        )

        # basic CodeBuild perms: CloudWatch Logs (create/write)
        # Note: The former AWS managed policy "service-role/AWSCodeBuildServiceRole"
        # is not attachable in this account; grant equivalent minimal perms inline.
        codebuild_role.add_to_policy(iam.PolicyStatement(
            actions=[
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents",
            ],
            resources=["*"],
        ))

        # perms for build stage (ECR push)
        codebuild_role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name(
                "AmazonEC2ContainerRegistryPowerUser"  # covers push/pull/create repo
            )
        )

        # perms for deploy stage (App Runner create/update)
        codebuild_role.add_to_policy(iam.PolicyStatement(
            actions=[
                "apprunner:ListServices",
                "apprunner:CreateService",
                "apprunner:UpdateService",
                "apprunner:DescribeService",
            ],
            resources=["*"],
        ))

        # allow CodeBuild to pass the ECR access role to App Runner
        # Remove service-conditional to avoid mismatches in iam:PassedToService
        # context; still restricted to the exact access role resource.
        codebuild_role.add_to_policy(iam.PolicyStatement(
            actions=["iam:PassRole"],
            resources=[ecr_access_role.role_arn],
        ))

        # allow CodeBuild to create App Runner service-linked role if needed
        codebuild_role.add_to_policy(iam.PolicyStatement(
            actions=["iam:CreateServiceLinkedRole"],
            resources=["*"],
            conditions={
                "StringEquals": {
                    "iam:AWSServiceName": "apprunner.amazonaws.com"
                }
            },
        ))


        # ----- Build (docker build + push; emits image.json) -----
        build_project = codebuild.PipelineProject(
            self, "Build",
            role=codebuild_role,
            environment=codebuild.BuildEnvironment(privileged=True),
            build_spec=codebuild.BuildSpec.from_source_filename("buildspec.yml"),
        )
        
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
            role=codebuild_role,
            environment=codebuild.BuildEnvironment(privileged=False),
            environment_variables={
                "ACCESS_ROLE_ARN": codebuild.BuildEnvironmentVariable(
                    value=ecr_access_role.role_arn
                    )
                    },
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
                            # 'aws iam create-service-linked-role --aws-service-name apprunner.amazonaws.com || true',
                            # resolve default access role if not provided by action env var
                            'ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)',
                            ': "${ACCESS_ROLE_ARN:?missing ACCESS_ROLE_ARN}"',
                            # build SourceConfiguration JSON safely
                            'SRC_CONFIG=$(python -c "import json,os; '
                            'print(json.dumps({'
                            '\'ImageRepository\':{\'ImageIdentifier\': os.environ[\'IMAGE\'], '
                            '\'ImageRepositoryType\':\'ECR\', '
                            '\'ImageConfiguration\':{\'Port\':\'8000\'}}, '
                            '\'AuthenticationConfiguration\':{\'AccessRoleArn\': os.environ[\'ACCESS_ROLE_ARN\']}, '
                            '\'AutoDeploymentsEnabled\': True}))")',
                            # create or update
                            'if [ -z "$SVC" ] || [ "$SVC" = "None" ]; then echo "Creating App Runner service ai-agents-portfolio"; SVC=$(aws apprunner create-service --service-name ai-agents-portfolio --source-configuration "$SRC_CONFIG" --query Service.ServiceArn --output text); else echo "Waiting for existing service to become ACTIVE"; aws apprunner wait service-active --service-arn "$SVC"; echo "Updating App Runner service $SVC"; aws apprunner update-service --service-arn "$SVC" --source-configuration "$SRC_CONFIG"; fi',
                            'echo "Waiting for service deployment to complete...";',
                            'aws apprunner wait service-active --service-arn "$SVC";',
                            # output service url
                            'aws apprunner describe-service --service-arn "$SVC" '
                            '  --query Service.ServiceUrl --output text'
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
                "ACCESS_ROLE_ARN": codebuild.BuildEnvironmentVariable(
                    value=ecr_access_role.role_arn   # NOT role/ai-agents
                )
            },
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

        # Allow CodeBuild projects to read/write pipeline artifacts in S3
        # (equivalent to the S3 access provided by the old managed policy)
        pipeline.artifact_bucket.grant_read_write(codebuild_role)

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
