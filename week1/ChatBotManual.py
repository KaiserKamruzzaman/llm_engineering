from scraper import fetch_website_contents
from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

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
        model="llama3.1:8b",
        messages=messages,
        stream=True
    )

    print("\nAssistant: ", end="", flush=True)
    reply = ""
    for chunk in response:
        content = chunk.choices[0].delta.content or ""
        print(content, end="", flush=True)
        reply += content
    print("\n")

    messages.append({"role": "assistant", "content": reply})
