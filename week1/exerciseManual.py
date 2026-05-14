import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

if api_key and api_key.startswith('sk-proj-') and len(api_key) > 10:
    print("API key looks good so far")
else:
    print("There might be a problem with your API key?")


# Connect to Ollama local server
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"  # dummy value
)



system_message = "You are a helpful assistant that explains concepts."
user_message = "newton laws of motion. Firsr law"

stream = client.chat.completions.create(
    model="gemma3:270m",
    messages=[
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message}
    ],
    stream=True
)

result = ""
for chunk in stream:
    delta = chunk.choices[0].delta.content or ""  # ✅ fixed
    print(delta, end="", flush=True)
    result += delta