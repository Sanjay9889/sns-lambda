import json
import json
import boto3

def lambda_handler(event, context):

    print("Printing Even")
    print(event)
    print("printing context")
    print(context)
    print("printing environment")
    print(os.environ)
    client = boto3.client('sns')
    response = client.publish(
        TargetArn='arn:aws:sns:us-east-1:499490402390:test_topic',
        Message=json.dumps({'default': 'Stay home', 'email': 'Please stay at home'}),
        Subject='Covid-19 update',
        MessageStructure='json'
    )

