import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_py.cdk_py_stack import CdkPyStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_py/cdk_py_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkPyStack(app, "cdk-py")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
