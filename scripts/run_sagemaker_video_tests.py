import base64, boto3, json, cv2, sys, os

sm = boto3.client("sagemaker-runtime", region_name="ap-south-1")
endpoint = os.getenv("SAGEMAKER_ENDPOINT", "homemindai-endpoint")

def extract_frame(video_path):
    cap = cv2.VideoCapture(video_path)
    ret, frame = cap.read()
    if not ret:
        print("Error reading frame"); sys.exit(1)
    cv2.imwrite("frame.jpg", frame)
    cap.release()
    return "frame.jpg"

frame = extract_frame(sys.argv[1])
with open(frame,"rb") as f:
    payload = {"image_base64": base64.b64encode(f.read()).decode()}
res = sm.invoke_endpoint(EndpointName=endpoint, ContentType="application/json", Body=json.dumps(payload))
print(res["Body"].read().decode())
