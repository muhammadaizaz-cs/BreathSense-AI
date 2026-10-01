from fastapi import FastAPI, UploadFile, File
import librosa
import numpy as np
import soundfile as sf

app = FastAPI()

@app.get("/")
def home():
    return {"message": "BreathSense AI backend is running"}

@app.post("/analyze")
async def analyze_audio(file: UploadFile = File(...)):
    # Save uploaded file
    audio_path = "temp.wav"
    
    with open(audio_path, "wb") as f:
        f.write(await file.read())

    # Load audio
    y, sr = librosa.load(audio_path, sr=22050)

    # Convert to simple features (temporary logic)
    energy = np.mean(np.abs(y))

    # Fake AI logic (we will replace with CNN later)
    if energy < 0.02:
        result = "Clear Breathing"
        risk = "Low"
    elif energy < 0.05:
        result = "Mild Wheeze Detected"
        risk = "Medium"
    else:
        result = "Severe Breathing Issue"
        risk = "High"

    return {
        "result": result,
        "risk_level": risk,
        "energy_score": float(energy)
    }