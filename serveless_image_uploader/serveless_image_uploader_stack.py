from aws_cdk import (
    core as cdk,
    aws_lambda as _lambda,
    aws_s3 as s3,
    aws_apigateway as apigw,
    aws_cloudfront as cloudfront,
    aws_s3_deployment as s3deploy,
    aws_cloudfront_origins as origins
)

class ServelessImageUploaderStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # S3
        images_bucket = s3.Bucket(
            self, 'ImagesBucket'
        )

        front_end_bucket = s3.Bucket(
            self, 'FrontEndBucket',
            public_read_access=True,
            website_index_document="index.html"
        )

        s3deploy.BucketDeployment(
            self, "DeployFrontEnd",
            sources=[s3deploy.Source.asset('./front-app/build')],
            destination_bucket=front_end_bucket
        )

        # CloudFront
        cloudfront.Distribution(
            self, "FrontEndDistribution",
            default_behavior=cloudfront.BehaviorOptions(origin=origins.S3Origin(front_end_bucket))
        )

        # Lambda
        hello_world_lambda = _lambda.Function(
            self, 'HelloWorldHandler',
            runtime=_lambda.Runtime.PYTHON_3_8,
            code=_lambda.Code.from_asset('lambda'),
            handler='hello_world.handler'
        )

        # API Gateway
        apigw.LambdaRestApi(
            self, "ApiGatewayEndpoint",
            handler=hello_world_lambda
        )
