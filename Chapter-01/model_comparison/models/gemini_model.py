import time
from google import genai
from google.genai import types
from config import GEMINI_API_KEY, GEMINI_MODEL

def call_gemini(prompt: str):
    client = genai.Client(api_key=GEMINI_API_KEY)

    # Set minimal thinking budget for low latency
    config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=1024)
    )

    start = time.time()
    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
        config=config
    )
    latency = time.time() - start

    return latency, response.text
