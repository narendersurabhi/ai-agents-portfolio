#!/usr/bin/env python3
import os
import aws_cdk as cdk
from cdk_py.pipeline_stack import PipelineStack

app = cdk.App()
PipelineStack(
    app, "AiAgentsPortfolioPipeline",
    env=cdk.Environment(
        account=os.environ.get("CDK_DEFAULT_ACCOUNT"),
        region=os.environ.get("CDK_DEFAULT_REGION"),
    ),
)
app.synth()
