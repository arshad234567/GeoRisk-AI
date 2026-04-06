from groq import Groq
import os
from dotenv import load_dotenv
from backend.agent.config import MODEL_NAME, TEMPERATURE
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def call_llm(messages):
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        temperature=TEMPERATURE,
    )
    return response.choices[0].message.content