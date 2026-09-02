from models import call_gemini, call_ollama, call_groq

# 1. Read prompt from prompt.txt
with open("prompt.txt", "r") as f:
    prompt = f.read().strip()

print(f"--- Shared Prompt ---\n{prompt}\n")

# 2. Define list of models to test
model_calls = [
    ("Closed Source : Google Gemini API", call_gemini),
    ("Open Source   : Local Ollama (Phi-3)", call_ollama),
    ("Reasoning     : Groq (GPT-OSS-120B)", call_groq),
]

# 3. Benchmark each model
for name, call_fn in model_calls:
    print(f"Testing {name}...")
    try:
        latency, output = call_fn(prompt)
        print(f"Latency: {latency:.2f}s")
        print(f"Output : {output}\n")
    except Exception as e:
        print(f"Error  : {e}\n")
