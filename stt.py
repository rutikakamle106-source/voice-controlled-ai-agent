from transformers import pipeline

stt_pipeline = pipeline("automatic-speech-recognition", model="openai/whisper-base")

def transcribe(audio_path):
    result = stt_pipeline(audio_path)
    return result["text"]