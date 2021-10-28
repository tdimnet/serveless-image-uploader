import os
import json
import base64
import uuid

import boto3
s3 = boto3.resource('s3')


def handler(event, context):
    bucket_name = os.environ.get('BUCKET_NAME')
    bucket = s3.Bucket(bucket_name)

    json_body = json.loads(event['body'])
    file_name = json_body['name']
    file_content = json_body['file']
    unique_id = uuid.uuid3(uuid.NAMESPACE_DNS, file_name)

    full_path = '{}/{}'.format(unique_id, file_name)

    bucket.put_object(
        Key=full_path,
        Body=base64.b64decode(file_content),
        ContentType='image/jpeg'
    )

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': 'success'
    }
