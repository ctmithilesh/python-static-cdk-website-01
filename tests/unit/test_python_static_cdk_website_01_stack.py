import aws_cdk as core
import aws_cdk.assertions as assertions

from python_static_cdk_website_01.python_static_cdk_website_01_stack import PythonStaticCdkWebsite01Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in python_static_cdk_website_01/python_static_cdk_website_01_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = PythonStaticCdkWebsite01Stack(app, "python-static-cdk-website-01")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
