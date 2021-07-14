import json
import json
import boto3

def lambda_handler(event, context):
    client = boto3.client('sns')
    response = client.publish(
        TargetArn='arn:aws:sns:us-east-1:499490402390:test_topic',
        Message=json.dumps({
            'email': 'Please stay inside home.'}),
        Subject='Covid-19 Update',
        MessageStructure='json'
    )

