import json
import os

import boto3
s3 = boto3.resource('s3')


def handler(event, context):
    print("Hello, world!")

    asset_bucket = s3.Bucket(os.environ.get('BUCKET_NAME'))

    print('List the objets in bucket {}'.format(asset_bucket))

    for my_bucket_object in asset_bucket.objects.all():
        print(my_bucket_object)

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': 'Hello, World from the AWS CDK'
    }
