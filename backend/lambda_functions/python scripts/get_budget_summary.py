import json
import boto3
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('BudgetItems')

def lambda_handler(event, context):
    response = table.scan()
    items = response.get('Items', [])

    total_income = Decimal('0')
    total_expense = Decimal('0')

    for item in items:
        amount = Decimal(str(item.get('amount', 0)))
        if item.get('type') == 'income':
            total_income += amount
        elif item.get('type') == 'expense':
            total_expense += amount

    summary = {
        'total_income': float(total_income),
        'total_expense': float(total_expense),
        'balance': float(total_income - total_expense)
    }

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(your_data)
    }