import os

import boto3

ddb = boto3.resource('dynamodb')

def handler(event, context):
    filename = event.get('file')
    ddb_table_name = os.environ.get('DDB_TABLE_NAME')

    ddb_table = ddb.Table(ddb_table_name)

    response = ddb_table.put_item(
        Item={
            'file_path': filename
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
