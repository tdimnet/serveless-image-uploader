import base64
import datetime
import json
import os

import boto3

s3 = boto3.resource('s3')
client = boto3.client('lambda')


def handler(event, context):
    bucket_name = os.environ.get('BUCKET_NAME')
    bucket = s3.Bucket(bucket_name)

    file_to_db_lambda = os.environ.get('FILE_TO_DB_LAMBDA')

    json_body = json.loads(event['body'])
    file_name = json_body['name']
    file_content = json_body['file']

    file_base_64 = ''

    if file_content.startswith('data:image/jpeg;base64,'):
        file_base_64 = base64.b64decode(file_content[23: ])
    else:
        file_base_64 = base64.b64decode(file_content)

    unique_id = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    full_path = '{}/{}'.format(unique_id, file_name)

    bucket.put_object(
        Key=full_path,
        Body=file_base_64,
        ContentType='image/jpg'
    )

    payload = {
        "file_name": file_name,
        "file_path": full_path,
        "datetime": unique_id
    }

    client.invoke(
        FunctionName=file_to_db_lambda,
        InvocationType='RequestResponse',
        Payload=json.dumps(payload)
    )

    image_url = 'https://{}.s3.amazonaws.com/{}'.format(bucket_name, full_path)

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/json',
            'Access-Control-Allow-Origin' : '*',
        },
        'body': json.dumps({
            'message': 'success',
            'image_path': image_url
        })
    }
