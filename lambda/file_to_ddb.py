def handler(event, context):
    print('Hello from file to dynamodb')

    print(event.get('file'))

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': 'success'
    }
