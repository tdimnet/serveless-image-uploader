def handler(event, context):
    print("Hello, world!")

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain',
            'Access-Control-Allow-Origin' : '*',
        },
        'body': 'Hello, World from the AWS CDK'
    }
