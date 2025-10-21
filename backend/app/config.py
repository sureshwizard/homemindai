import os

AWS_REGION = os.getenv("AWS_REGION", "ap-south-1")
SAGEMAKER_ENDPOINT = os.getenv("SAGEMAKER_ENDPOINT", "homemindai-endpoint")
ARTIFACT_BUCKET = os.getenv("ARTIFACT_BUCKET", "")
SNS_TOPIC_ARN = os.getenv("SNS_TOPIC_ARN", "")
IOT_TOPIC = "homemind/devices/command"
