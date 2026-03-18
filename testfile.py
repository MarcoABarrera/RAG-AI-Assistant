from dotenv import load_dotenv
import os
from openai import OpenAI

# Load .env file
load_dotenv()

# Initialize client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Hello!"}]
)

print(response.choices[0].message.content)
print(os.getenv("OPENAI_API_KEY"))