# app/whisper_transcriber.py
import whisper

def transcribe_audio(filename: str) -> str:
    model = whisper.load_model("base")
    result = model.transcribe(filename, language="uk")
    return result["text"]

