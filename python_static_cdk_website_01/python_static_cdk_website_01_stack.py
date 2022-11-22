from aws_cdk import (
    Duration,
    Stack,
    aws_sqs as sqs,
    aws_s3 as s3, 
    aws_s3_deployment as s3deploy
)
from constructs import Construct

class PythonStaticCdkWebsite01Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
    # example resource
        queue = sqs.Queue(
            self, "TeslaPythonSite01Queue",
            visibility_timeout=Duration.seconds(300),
        )
        
        bucket = s3.Bucket(
            self, 
            "MyFirstBucket", 
            website_index_document="index.html",
            public_read_access=True,
           
        )
        
        deployment = s3deploy.BucketDeployment(
            self, 
            "DeployWebsite",
             sources=[s3deploy.Source.asset('website')],
            destination_bucket=bucket
)
