import boto3, json, tempfile
from .sagemaker_client import invoke_sagemaker
from .config import SAGEMAKER_ENDPOINT

async def process_uploaded_video(file):
    temp = tempfile.NamedTemporaryFile(delete=False)
    contents = await file.read()
    temp.write(contents)
    temp.close()

    # Simulated frame → analysis
    result = invoke_sagemaker(temp.name, SAGEMAKER_ENDPOINT)
    return {"event_detected": result.get("label", "unknown"), "confidence": result.get("confidence", 0.0)}
