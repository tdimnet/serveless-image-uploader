from ddtrace import tracer
from datadog_lambda.metric import lambda_metric

def handler(event, context):
    current_span = tracer.current_span()
    
    with tracer.trace('hello.world'):
        print("Hello, world!")

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain',
            'Access-Control-Allow-Origin' : '*',
        },
        'body': 'Hello, World from the AWS CDK'
    }
