import numpy as np
import librosa

def predict_audio(file_path):

    y, sr = librosa.load(file_path, sr=22050)

    # fake simple logic (replace with CNN later)
    energy = np.mean(np.abs(y))

    if energy < 0.02:
        label = "Normal"
        risk = "Low"
    elif energy < 0.05:
        label = "Wheeze"
        risk = "Medium"
    else:
        label = "Severe"
        risk = "High"

    return {
        "prediction": label,
        "risk": risk,
        "confidence": 85
    }