import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as codepipeline from 'aws-cdk-lib/aws-codepipeline';
import * as actions from 'aws-cdk-lib/aws-codepipeline-actions';
import * as codebuild from 'aws-cdk-lib/aws-codebuild';

export class PipelineStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Parameters
    const connectionArn = new cdk.CfnParameter(this, 'GitHubConnectionArn', { type: 'String' });
    const owner = new cdk.CfnParameter(this, 'RepoOwner', { type: 'String' });
    const repo = new cdk.CfnParameter(this, 'RepoName', { type: 'String' });
    const branch = new cdk.CfnParameter(this, 'Branch', { type: 'String', default: 'main' });

    // Minimal pipeline (Source -> Build only; add Deploy later)
    const sourceOut = new codepipeline.Artifact();
    const source = new actions.CodeStarConnectionsSourceAction({
      actionName: 'GitHub',
      owner: owner.valueAsString,
      repo: repo.valueAsString,
      branch: branch.valueAsString,
      connectionArn: connectionArn.valueAsString,
      output: sourceOut,
      codeBuildCloneOutput: true,
      triggerOnPush: true,
    });

    const project = new codebuild.PipelineProject(this, 'Build', {
      environment: { privileged: true },
      buildSpec: codebuild.BuildSpec.fromSourceFilename('buildspec.yml'),
    });

    const build = new actions.CodeBuildAction({
      actionName: 'Build',
      input: sourceOut,
      project,
    });

    new codepipeline.Pipeline(this, 'AiAgentsPortfolio', {
      stages: [
        { stageName: 'Source', actions: [source] },
        { stageName: 'Build', actions: [build] },
      ],
    });
  }
}
