import json
import boto3
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('BudgetItems')

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return super(DecimalEncoder, self).default(obj)

def lambda_handler(event, context):
    # Get item_id from path parameters
    item_id = event['pathParameters']['item_id']
    response = table.get_item(Key={'item_id': item_id})
    item = response.get('Item')
    if item:
        return {
            'statusCode': 200,
            'body': json.dumps(item, cls=DecimalEncoder)
        }
    else:
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps(your_data)
        }