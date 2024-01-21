import boto3
from botocore.exceptions import ClientError
 
def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('employee')
 
    try:
        response = table.update_item(
            Key={'id': 3},
            UpdateExpression="SET salary = :s",
            ExpressionAttributeValues={':s': 6000},
            ReturnValues="UPDATED_NEW"
        )
        print(response['Attributes'])
        return {
            'statusCode': 200,
            'body': 'Item updated successfully'
        }
    except ClientError as e:
        print(f"Error updating item: {e}")
        return {
            'statusCode': 500,
            'body': f'Error updating item: {e}'
        }
