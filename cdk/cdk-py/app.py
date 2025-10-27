#!/usr/bin/env python3
import os, aws_cdk as cdk
from cdk_py.pipeline_stack import PipelineStack

acct = os.environ.get("CDK_DEFAULT_ACCOUNT")
region = os.environ.get("CDK_DEFAULT_REGION")
if not acct or not region:
    raise RuntimeError("Set CDK_DEFAULT_ACCOUNT and CDK_DEFAULT_REGION before running CDK.")

app = cdk.App()
PipelineStack(app, "AiAgentsPortfolioPipeline",
              env=cdk.Environment(account=acct, region=region))
app.synth()
