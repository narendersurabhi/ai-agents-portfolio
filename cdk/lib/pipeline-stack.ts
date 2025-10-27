import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as codepipeline from 'aws-cdk-lib/aws-codepipeline';
import * as actions from 'aws-cdk-lib/aws-codepipeline-actions';
import * as codebuild from 'aws-cdk-lib/aws-codebuild';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as sns from 'aws-cdk-lib/aws-sns';
import * as notif from 'aws-cdk-lib/aws-codestarnotifications';

export class PipelineStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const connectionArn = new cdk.CfnParameter(this, 'GitHubConnectionArn', { type: 'String' });
    const owner = new cdk.CfnParameter(this, 'RepoOwner', { type: 'String' });
    const repo = new cdk.CfnParameter(this, 'RepoName', { type: 'String', default: 'ai-agents-portfolio' });
    const branch = new cdk.CfnParameter(this, 'Branch', { type: 'String', default: 'main' });

    const sourceOutput = new codepipeline.Artifact();
    const source = new actions.CodeStarConnectionsSourceAction({
      actionName: 'GitHub',
      owner: owner.valueAsString,
      repo: repo.valueAsString,
      branch: branch.valueAsString,
      connectionArn: connectionArn.valueAsString,
      output: sourceOutput,
      codeBuildCloneOutput: true, // enables GitHub Checks + status in CodeBuild
      triggerOnPush: true
    });

    const project = new codebuild.PipelineProject(this, 'Build', {
      environment: {
        privileged: true // for Docker
      },
      buildSpec: codebuild.BuildSpec.fromSourceFilename('buildspec.yml')
    });

    // Report build status back to GitHub
    project.bindToCodePipeline(project);
    project.addToRolePolicy(new iam.PolicyStatement({
      actions: ['ecr:*', 'sts:GetCallerIdentity'],
      resources: ['*']
    }));

    const buildOutput = new codepipeline.Artifact();
    const build = new actions.CodeBuildAction({
      actionName: 'BuildAndPush',
      input: sourceOutput,
      project,
      outputs: [buildOutput]
    });

    // Simple deploy: update App Runner image using CLI
    const deployProject = new codebuild.PipelineProject(this, 'Deploy', {
      buildSpec: codebuild.BuildSpec.fromObject({
        version: '0.2',
        phases: { build: { commands: [
          'IMAGE=$(cat image.json | jq -r .imageUri)',
          // create once; later calls update
          'ARN=$(aws apprunner list-services --query "ServiceSummaryList[?ServiceName==\'ai-agents-portfolio\'].ServiceArn" --output text)',
          'if [ -z "$ARN" ]; then aws apprunner create-service --service-name ai-agents-portfolio --source-configuration "{\"ImageRepository\":{\"ImageIdentifier\":\"$IMAGE\",\"ImageRepositoryType\":\"ECR\",\"ImageConfiguration\":{\"Port\":\"8080\"}},\"AutoDeploymentsEnabled\":true}" ; else aws apprunner update-service --service-arn "$ARN" --source-configuration "{\"ImageRepository\":{\"ImageIdentifier\":\"$IMAGE\",\"ImageRepositoryType\":\"ECR\",\"ImageConfiguration\":{\"Port\":\"8080\"}}}"; fi',
          'aws apprunner describe-service --service-arn $(aws apprunner list-services --query "ServiceSummaryList[?ServiceName==\'ai-agents-portfolio\'].ServiceArn" --output text) --query Service.ServiceUrl --output text'
        ]}},
        artifacts: { files: ['image.json'] }
      })
    });
    deployProject.addToRolePolicy(new iam.PolicyStatement({ actions: ['apprunner:*'], resources: ['*'] }));

    const deploy = new actions.CodeBuildAction({
      actionName: 'Deploy',
      input: buildOutput,
      project: deployProject
    });

    const pipeline = new codepipeline.Pipeline(this, 'Pipeline', {
      pipelineName: 'AiAgentsPortfolio',
      restartExecutionOnUpdate: true,
      stages: [
        { stageName: 'Source', actions: [source] },
        { stageName: 'Build', actions: [build] },
        { stageName: 'Deploy', actions: [deploy] }
      ]
    });

    // Notifications: email/Slack via SNS + CodeStar Notifications
    const topic = new sns.Topic(this, 'PipelineTopic');
    new notif.NotificationRule(this, 'PipelineNotifications', {
      source: pipeline,
      events: [
        'codepipeline-pipeline-pipeline-execution-started',
        'codepipeline-pipeline-pipeline-execution-succeeded',
        'codepipeline-pipeline-pipeline-execution-failed',
        'codepipeline-pipeline-action-execution-failed'
      ],
      targets: [notif.NotificationTarget.fromTopic(topic)]
    });

    new cdk.CfnOutput(this, 'SNSTopicArn', { value: topic.topicArn });
  }
}
