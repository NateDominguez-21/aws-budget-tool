import json
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('BudgetItems')

def lambda_handler(event, context):
    # Parse input
    body = json.loads(event['body'])
    item_type = body['type']
    amount = body['amount']
    description = body.get('description', '')
    date = body.get('date', datetime.utcnow().strftime('%Y-%m-%d'))

    # Generate unique ID
    item_id = str(uuid.uuid4())

    # Put item in DynamoDB
    table.put_item(
        Item={
            'item_id': item_id,
            'type': item_type,
            'amount': amount,
            'description': description,
            'date': date
        }
    )

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(your_data)
    }