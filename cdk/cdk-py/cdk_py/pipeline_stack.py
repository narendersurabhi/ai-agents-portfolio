from aws_cdk import (
    Stack, CfnParameter, Duration, aws_codepipeline as codepipeline,
    aws_codepipeline_actions as actions, aws_codebuild as codebuild,
    aws_iam as iam, #aws_sns as sns, aws_codestarnotifications as notif,
)
from aws_cdk import aws_sns as sns, aws_events as events, aws_events_targets as targets
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

        # Build (docker build + push; outputs image.json)
        build_project = codebuild.PipelineProject(
            self, "Build",
            environment=codebuild.BuildEnvironment(privileged=True),
            build_spec=codebuild.BuildSpec.from_source_filename("buildspec.yml"),
        )
        build_project.add_to_role_policy(iam.PolicyStatement(
            actions=["ecr:*","sts:GetCallerIdentity"],
            resources=["*"]
        ))

        build = actions.CodeBuildAction(
            action_name="BuildAndPush",
            input=source_out,
            outputs=[build_out],
            project=build_project
        )

        # IAM role for App Runner to pull private ECR images
        ecr_access_role = iam.Role(
            self,
            "AppRunnerEcrAccessRole",
            assumed_by=iam.ServicePrincipal("build.apprunner.amazonaws.com"),
            description="Role that App Runner uses to pull from private ECR",
        )
        ecr_access_role.add_to_policy(iam.PolicyStatement(
            actions=[
                "ecr:GetAuthorizationToken",
                "ecr:BatchCheckLayerAvailability",
                "ecr:GetDownloadUrlForLayer",
                "ecr:BatchGetImage",
            ],
            resources=["*"]
        ))

        # Deploy (App Runner create/update)
        deploy_project = codebuild.PipelineProject(
            self, "Deploy",
            build_spec=codebuild.BuildSpec.from_object({
                "version": "0.2",
                "env": {"variables": {"ACCESS_ROLE_ARN": ecr_access_role.role_arn}},
                "phases": {
                    "build": {"commands": [
                        "IMAGE=$(jq -r .imageUri image.json)",
                        "SVC=$(aws apprunner list-services --query \"ServiceSummaryList[?ServiceName=='ai-agents-portfolio'].ServiceArn\" --output text)",
                        "aws iam create-service-linked-role --aws-service-name apprunner.amazonaws.com || true",
                        "SRC_CONFIG=$(jq -n --arg img \"$IMAGE\" --arg arn \"$ACCESS_ROLE_ARN\" '{ImageRepository:{ImageIdentifier:$img,ImageRepositoryType:\"ECR\",ImageConfiguration:{Port:\"8080\"}},AuthenticationConfiguration:{AccessRoleArn:$arn},AutoDeploymentsEnabled:true}')",
                        "if [ -z \"$SVC\" ]; then aws apprunner create-service --service-name ai-agents-portfolio --source-configuration \"$SRC_CONFIG\"; else aws apprunner update-service --service-arn \"$SVC\" --source-configuration \"$SRC_CONFIG\"; fi",
                        "aws apprunner describe-service --service-arn $(aws apprunner list-services --query \"ServiceSummaryList[?ServiceName=='ai-agents-portfolio'].ServiceArn\" --output text) --query Service.ServiceUrl --output text"
                    ]}
                },
                "artifacts": {"files": ["image.json"]}
            }),
            timeout=Duration.minutes(15)
        )
        
        deploy_project.add_to_role_policy(iam.PolicyStatement(
            actions=["apprunner:*"],
            resources=["*"]
        ))

        # Allow creation of the App Runner service-linked role on first use.
        # Some regions/accounts report different service names, so allow both.
        deploy_project.add_to_role_policy(iam.PolicyStatement(
            actions=["iam:CreateServiceLinkedRole"],
            resources=["*"],
            conditions={"StringEquals": {"iam:AWSServiceName": [
                "apprunner.amazonaws.com",
                "build.apprunner.amazonaws.com"
            ]}}
        ))

        # Proactively ensure the App Runner service-linked role exists to avoid
        # requiring CreateServiceLinkedRole at deploy time.
        iam.CfnServiceLinkedRole(self, "AppRunnerSLR", aws_service_name="apprunner.amazonaws.com")

        # Attach a managed policy that covers App Runner deploy operations, including
        # creating the service-linked role on first use.
        if deploy_project.role is not None:
            deploy_project.role.add_managed_policy(
                iam.ManagedPolicy.from_aws_managed_policy_name("AWSAppRunnerFullAccess")
            )
            # Allow passing the ECR access role to App Runner (cover both service values)
            deploy_project.add_to_role_policy(iam.PolicyStatement(
                actions=["iam:PassRole"],
                resources=[ecr_access_role.role_arn],
                conditions={"StringEquals": {"iam:PassedToService": [
                    "apprunner.amazonaws.com",
                    "build.apprunner.amazonaws.com"
                ]}}
            ))

        deploy = actions.CodeBuildAction(
            action_name="Deploy",
            input=build_out,
            project=deploy_project
        )


        pipeline = codepipeline.Pipeline(
            self, "AiAgentsPortfolio",
            stages=[
                codepipeline.StageProps(stage_name="Source", actions=[source]),
                codepipeline.StageProps(stage_name="Build", actions=[build]),
                codepipeline.StageProps(stage_name="Deploy", actions=[deploy]),
            ]
        )


        topic = sns.Topic(self, "PipelineTopic")

        events.Rule(
            self, "PipelineEventRule",
            event_pattern=events.EventPattern(
                source=["aws.codepipeline"],
                detail_type=[
                    "CodePipeline Pipeline Execution State Change",
                    "CodePipeline Action Execution State Change"
                ],
                detail={"pipeline": [pipeline.pipeline_name]},
            ),
            targets=[targets.SnsTopic(topic)],
        )

        # # Notifications (SNS target; add email/Slack later)
        # topic = sns.Topic(self, "PipelineTopic")

        # notif.NotificationRule(
        #     self, "PipelineNotifications",
        #     source=pipeline,
        #     events=[
        #         "codepipeline-pipeline-pipeline-execution-started",
        #         "codepipeline-pipeline-pipeline-execution-succeeded",
        #         "codepipeline-pipeline-pipeline-execution-failed",
        #         "codepipeline-pipeline-action-execution-failed",
        #     ],
        #     targets=[notif.SnsTopic(topic)],
        # )

