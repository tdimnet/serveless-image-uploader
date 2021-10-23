from aws_cdk import (
    core as cdk,
    aws_lambda as _lambda
)


class ServelessImageUploaderStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        hello_world_lambda = _lambda.Function(
            self, 'HelloWorldHandler',
            runtime=_lambda.Runtime.PYTHON_3_8,
            code=_lambda.Code.from_asset('lambda'),
            handler='hello_world.handler'
        )
