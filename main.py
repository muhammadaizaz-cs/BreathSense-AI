from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import shutil
from predict import predict_audio

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze_audio(file: UploadFile = File(...)):
    path = f"temp.wav"

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = predict_audio(path)

    return result