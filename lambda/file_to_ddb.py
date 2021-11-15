from datetime import datetime
import os

import boto3

ddb = boto3.resource('dynamodb')

def handler(event, context):
    file_path = event.get('file_path')
    file_name = event.get('file_name')
    file_datetime = event.get('datetime')

    ddb_table_name = os.environ.get('DDB_TABLE_NAME')
    ddb_table = ddb.Table(ddb_table_name)

    response = ddb_table.put_item(
        Item={
            'file_path': file_path,
            'file_name': file_name,
            'image_type': 'jpg',
            "file_datetime": file_datetime
        }
    )

    status_code = response['ResponseMetadata']['HTTPStatusCode']

    return {
        'statusCode': status_code,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': 'Write to DynamoDB Succed'
    }
