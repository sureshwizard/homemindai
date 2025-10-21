from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from .events import process_uploaded_video
from .config import AWS_REGION

app = FastAPI(title="HomeMindAI Backend", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/status")
def status():
    return {"status": "running", "region": AWS_REGION}

@app.post("/api/upload")
async def upload_video(file: UploadFile = File(...)):
    return await process_uploaded_video(file)
