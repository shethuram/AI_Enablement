import time
from groq import Groq
from config import GROQ_API_KEY, GROQ_MODEL

def call_groq(prompt: str):
    client = Groq(api_key=GROQ_API_KEY)

    start = time.time()
    # Configure high reasoning effort for GPT-OSS model
    response = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[{"role": "user", "content": prompt}],
        reasoning_effort="high"
    )
    latency = time.time() - start

    output = response.choices[0].message.content
    return latency, output
