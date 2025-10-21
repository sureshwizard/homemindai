import boto3, json
from .config import IOT_TOPIC

def send_iot_command(device_id, action):
    client = boto3.client("iot-data")
    payload = json.dumps({"device": device_id, "action": action})
    client.publish(topic=IOT_TOPIC, qos=0, payload=payload)
    return {"sent": True, "action": action}
