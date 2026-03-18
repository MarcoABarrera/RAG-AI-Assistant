from dotenv import load_dotenv
import os
print("FILES:", os.listdir())
# Force correct path
env_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path=env_path)

print("DEBUG KEY:", os.getenv("OPENAI_API_KEY"))