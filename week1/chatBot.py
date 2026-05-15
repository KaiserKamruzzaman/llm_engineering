import os
import sys
from dotenv import load_dotenv
from scraper import fetch_website_contents
from openai import OpenAI

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

if not api_key:
    print("No API key was found - please head over to the troubleshooting notebook in this folder to identify & fix!")
    sys.exit(1)
elif not api_key.startswith("sk-proj-"):
    print("An API key was found, but it doesn't start sk-proj-; please check you're using the right key - see troubleshooting notebook")
    sys.exit(1)
else:
    print("API key found and looks good so far!")

client = OpenAI()

print("Fetching portfolio data...")
website_content = fetch_website_contents("https://kaiserkamruzzaman.com")

system_message = (
    f"You are a helpful assistant for Kaiser Kamruzzaman's portfolio website. "
    f"Answer questions about his skills, experience, and projects based on the website content below. "
    f"You can also respond to greetings naturally. Be concise and friendly.\n\n"
    f"Website content:\n{website_content}"
)

messages = [{"role": "system", "content": system_message}]

print("\nChatbot ready! Ask me anything about Kaiser's portfolio. Type 'quit' to exit.\n")

while True:
    user_input = input("You: ").strip()

    if not user_input:
        continue
    if user_input.lower() in ("quit", "exit", "bye"):
        print("Goodbye!")
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})

    print(f"\nAssistant: {reply}\n")
