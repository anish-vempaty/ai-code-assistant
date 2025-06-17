import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

def review_code(content, filename):
    prompt = f"You are a senior software engineer. Review this code in {filename} and suggest improvements. Return the updated version or say 'NO CHANGES REQUIRED'.\n\n" + content

    response = model.generate_content(prompt)
    return response.text.strip()