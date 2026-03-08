import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
MODEL = os.getenv("MODEL_NAME", "deepseek-chat")
API_KEY = os.getenv("DEEPSEEK_API_KEY")
BASE_URL = os.getenv("BASE_URL", "https://api.deepseek.com")

class LLMClient:
    def __init__(self):
        self.client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

    def generate(self, prompt: str, temperature: float = 0):
        response = self.client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
        )

        return response.choices[0].message.content