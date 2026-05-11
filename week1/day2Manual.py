from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-5-nano",
    messages=[
        {
            "role": "user",
            "content": "Tell me a fun fact"
        }
    ]
)

print(response.choices[0].message.content)