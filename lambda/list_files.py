import os
import json

import boto3

s3 = boto3.resource('s3')
ddb = boto3.resource('dynamodb')


def handler(event, context):
    ddb_table_name = os.environ.get('DDB_TABLE')
    cdn_name = os.environ.get('IMAGES_CDN')

    ddb_table = ddb.Table(ddb_table_name)
    table_data = ddb_table.scan()
    
    images = []
    for image in table_data['Items']:
        image_path = image['file_path']
        images.append(
            '{}/{}'.format(cdn_name, image_path)
        )

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/json',
            'Access-Control-Allow-Origin' : '*',
        },
        'body': json.dumps({
            'message': 'success',
            'images': images
        })
    }
