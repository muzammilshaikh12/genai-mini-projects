# app/services/gemini_utils.py
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def generate_gemini_response(prompt: str):
    response = model.generate_content(prompt)
    return response.text
