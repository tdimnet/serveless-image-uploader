import os
import json

import boto3

s3 = boto3.resource('s3')
ddb = boto3.resource('dynamodb')


def handler(event, context):
    bucket_name = os.environ.get('BUCKET_NAME')
    ddb_table_name = os.environ.get('DDB_TABLE')

    ddb_table = ddb.Table(ddb_table_name)
    table_data = ddb_table.scan()
    
    images = []
    for image in table_data['Items']:
        image_path = image['file_path']
        images.append(
            'https://{}.s3.amazonaws.com/{}'.format(bucket_name, image_path)
        )

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/json'
        },
        'body': json.dumps({
            'message': 'success',
            'images': images
        })
    }
