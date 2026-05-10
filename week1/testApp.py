from openai import OpenAI

# Connect to Ollama local server
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"  # dummy value
)
website = "https://kaiserkamruzzaman.com"

system_prompt = """
You are a helpful assistant that summarizes websites.
Respond in markdown.
"""

user_prompt = """
Help me summarize this website content.
"""


messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt + "\n\n" + website}
]

response = client.chat.completions.create(
    model="gemma3:270m",
    messages=messages
)

print(response.choices[0].message.content)