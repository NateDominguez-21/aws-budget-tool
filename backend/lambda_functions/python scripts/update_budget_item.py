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
    item_id = event['pathParameters']['item_id']
    body = json.loads(event['body'])

    # Prepare update expression and attribute values
    update_expression = "SET "
    expression_attribute_values = {}
    expression_attribute_names = {}
    updates = []
    for key in ['type', 'amount', 'description', 'date']:
        if key in body:
            updates.append(f"#{key} = :{key}")
            expression_attribute_values[f":{key}"] = body[key]
            expression_attribute_names[f"#{key}"] = key
    update_expression += ", ".join(updates)

    # Update the item
    response = table.update_item(
        Key={'item_id': item_id},
        UpdateExpression=update_expression,
        ExpressionAttributeValues=expression_attribute_values,
        ExpressionAttributeNames=expression_attribute_names,
        ReturnValues="ALL_NEW"
    )

    updated_item = response.get('Attributes', {})
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(your_data)
    }