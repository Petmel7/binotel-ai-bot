# app/main.py
import os
import requests
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from app.whisper_transcriber import transcribe_audio
from app.analyzer import analyze_call_gemini
from app.telegram_bot import send_to_telegram

load_dotenv()
app = Flask(__name__)

def download_audio(url: str, filename: str = "call.wav") -> str:
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)
    return filename

@app.route("/webhook", methods=["POST"])
def binotel_webhook():
    data = request.json
    audio_url = data.get("audio_url")
    if not audio_url:
        return jsonify({"error": "No audio_url provided"}), 400
    try:
        audio_file = download_audio(audio_url)
        transcript = transcribe_audio(audio_file)
        analysis = analyze_call_gemini(transcript)
        send_to_telegram(analysis)
        return jsonify({"status": "processed"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

