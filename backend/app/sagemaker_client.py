import boto3, json, base64

def invoke_sagemaker(frame_path, endpoint_name):
    sm = boto3.client("sagemaker-runtime")
    with open(frame_path, "rb") as f:
        payload = {"image_base64": base64.b64encode(f.read()).decode()}
    res = sm.invoke_endpoint(EndpointName=endpoint_name, ContentType="application/json", Body=json.dumps(payload))
    try:
        return json.loads(res["Body"].read().decode())
    except:
        return {"label": "error", "confidence": 0}
