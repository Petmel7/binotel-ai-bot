# app/analyzer.py
import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def analyze_call_gemini(transcript: str) -> str:
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [{"parts": [{"text": (
            "Проаналізуй наступну розмову менеджера з клієнтом. "
            "Вкажи основні помилки, пропозиції як покращити розмову, "
            "як можна підвищити ефективність продажів.\n\n" + transcript
        )}]}],
        "generationConfig": {"temperature": 0.7}
    }
    params = {"key": GEMINI_API_KEY}
    response = requests.post(url, json=payload, headers=headers, params=params)
    result = response.json()
    return result['candidates'][0]['content']['parts'][0]['text']

