import os

import boto3
s3 = boto3.resource('s3')


def handler(event, context):
    print("Call list_files lambda function")

    bucket = s3.Bucket(os.environ.get('BUCKET_NAME'))

    print("List the objets in the bucket {}".format(bucket))

    for object in bucket.objects.all():
        print("=====")
        print(object)
        print("=====")

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': 'Fetching all images in bucket in {}'.format(bucket)
    }
