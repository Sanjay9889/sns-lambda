import json
import json
import boto3

def lambda_handler(event, context):
    message = {"foo": "bar"}
    client = boto3.client('sns')
    response = client.publish(
        TargetArn='arn:aws:sns:us-east-1:499490402390:test_topic',
        Message=json.dumps({'default': json.dumps(message),
                            'sms': 'here a short version of the message',
                            'email': 'here a longer version of the message'}),
        Subject='a short subject for your message',
        MessageStructure='json'
    )

