import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('BudgetItems')

def lambda_handler(event, context):
    item_id = event['pathParameters']['item_id']
    response = table.delete_item(
        Key={'item_id': item_id},
        ReturnValues='ALL_OLD'
    )
    deleted_item = response.get('Attributes')
    if deleted_item:
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Item deleted', 'item': deleted_item})
        }
    else:
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps(your_data)
        }