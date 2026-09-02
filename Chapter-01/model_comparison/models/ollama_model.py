import time
import requests
from config import OLLAMA_HOST, OLLAMA_MODEL

def call_ollama(prompt: str):
    url = f"{OLLAMA_HOST}/api/generate"
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False
    }

    start = time.time()
    response = requests.post(url, json=payload)
    latency = time.time() - start

    response.raise_for_status()
    result = response.json()
    return latency, result.get("response", "")
