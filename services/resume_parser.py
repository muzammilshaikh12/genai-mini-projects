import os
import tempfile
import fitz  # PyMuPDF
import google.generativeai as genai
from dotenv import load_dotenv
from prompts.resume_parser_prompt import resume_parsing_prompt
from utils.json_cleaner import extract_clean_json
import json
import re

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(
    "gemini-1.5-flash",
    generation_config=genai.types.GenerationConfig(
        temperature=0.2,
        top_k=20,
        top_p=0.8,
        max_output_tokens=512
    )
)

def extract_text_from_pdf(file_bytes: bytes) -> str:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(file_bytes)
        tmp_path = tmp.name

    doc = fitz.open(tmp_path)
    full_text = ""
    for page in doc:
        full_text += page.get_text() + "\n"
    doc.close()
    os.remove(tmp_path)
    return full_text.strip()


def parse_resume_from_text(text: str) -> str:
    prompt = resume_parsing_prompt.format(text=text)
    try:
        response = model.generate_content(prompt)
        return extract_clean_json(response.text)
    except Exception as e:
        return f"Error: {e}"
