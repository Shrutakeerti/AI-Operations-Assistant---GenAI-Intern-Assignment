import os
import time
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
model_name = os.getenv("GROQ_MODEL_NAME")

if not api_key:
    raise RuntimeError("GROQ_API_KEY not found")

if not model_name:
    raise RuntimeError("GROQ_MODEL_NAME not found")

client = Groq(
    api_key=api_key,
    timeout=60.0,
)

def call_llm(prompt, temperature=0, retries=3):

    for attempt in range(retries):
        try:
            response = client.chat.completions.create(
                model=model_name,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
            )

            return response.choices[0].message.content

        except Exception as e:
            print(f"⚠️ Groq timeout retry {attempt+1}/{retries}")
            time.sleep(2)

    raise RuntimeError("Groq API failed after retries")
