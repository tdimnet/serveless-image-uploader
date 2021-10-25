import os

import boto3
s3 = boto3.resource('s3')


def handler(event, context):
    bucket = s3.Bucket(os.environ.get('BUCKET_NAME'))

    # txt_data = b'This is the content of the file uploaded from python boto3 asdfasdf'

    # object = s3.Object(asset_bucket, 'file_name.txt')
    # result = object.put(Body=txt_data)


    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': 'Prepare to upload file in {}'.format(bucket)
    }
