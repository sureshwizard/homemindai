import boto3, os, json, base64
sm = boto3.client("sagemaker-runtime")

def handler(event, context):
    if not os.getenv("SAGEMAKER_ENDPOINT"):
        return {"statusCode":500,"body":"No endpoint set"}
    payload = json.dumps(event)
    res = sm.invoke_endpoint(EndpointName=os.getenv("SAGEMAKER_ENDPOINT"), ContentType="application/json", Body=payload)
    return {"statusCode":200,"body":res["Body"].read().decode()}
