import boto3, json, os
sns = boto3.client("sns")

def handler(event, context):
    print("Event received:", event)
    msg = json.dumps(event)
    topic = os.getenv("SNS_TOPIC_ARN")
    if topic:
        sns.publish(TopicArn=topic, Message=msg, Subject="HomeMindAI Event")
    return {"statusCode":200, "body": msg}
