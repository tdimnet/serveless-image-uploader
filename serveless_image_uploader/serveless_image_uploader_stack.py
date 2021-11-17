from aws_cdk import (
    core as cdk,
    aws_lambda as _lambda,
    aws_s3 as s3,
    aws_apigateway as apigw,
    aws_cloudfront as cloudfront,
    aws_s3_deployment as s3deploy,
    aws_cloudfront_origins as origins,
    aws_dynamodb as ddb,
)


class ServelessImageUploaderStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # S3
        images_bucket = s3.Bucket(
            self, 'ImagesBucket',
            public_read_access=True
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
        images_cdn = cloudfront.Distribution(
            self, "ImagesDistribution",
            default_behavior=cloudfront.BehaviorOptions(origin=origins.S3Origin(images_bucket))
        )

        # DynamoDB
        file_table = ddb.Table(
            self, "FileTable",
            partition_key={
                'name': 'file_path',
                'type': ddb.AttributeType.STRING
            }
        )

        # Lambda
        hello_world_lambda = _lambda.Function(
            self, 'HelloWorldHandler',
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset('lambda'),
            handler='hello_world.handler'
        )
        
        list_files_lambda = _lambda.Function(
            self, 'ListFilesHandler',
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset('lambda'),
            handler='list_files.handler',
            environment=dict(
                DDB_TABLE=file_table.table_name,
                IMAGES_CDN=images_cdn.domain_name
            )
        )

        file_to_ddb_lambda = _lambda.Function(
            self, 'FileToDDBHandler',
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset('lambda'),
            handler='file_to_ddb.handler',
            environment=dict(
                DDB_TABLE_NAME=file_table.table_name
            )
        )

        upload_file_lambda = _lambda.Function(
            self, 'UploadFileHandler',
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset('lambda'),
            handler='upload_file.handler',
            environment=dict(
                BUCKET_NAME=images_bucket.bucket_name,
                FILE_TO_DB_LAMBDA=file_to_ddb_lambda.function_name
            )
        )

        # API Gateway
        api = apigw.RestApi(
            self, 'Api',
            default_cors_preflight_options={
                "allow_origins": apigw.Cors.ALL_ORIGINS,
                "allow_methods": apigw.Cors.ALL_METHODS
            }
        )

        # Hello World Api Example
        hello_api = api.root.add_resource('hello')
        hello_api.add_method(
            'GET',
            apigw.LambdaIntegration(hello_world_lambda)
        )

        # Images Api
        images_api = api.root.add_resource('images')
        
        images_api.add_method(
            'GET',
            apigw.LambdaIntegration(list_files_lambda)
        )

        images_api.add_method(
            'POST',
            apigw.LambdaIntegration(upload_file_lambda)
        )

        # Grant access to resources
        images_bucket.grant_read(list_files_lambda)
        images_bucket.grant_write(upload_file_lambda)

        file_to_ddb_lambda.grant_invoke(upload_file_lambda)

        file_table.grant_write_data(file_to_ddb_lambda)
        file_table.grant_read_data(list_files_lambda)
