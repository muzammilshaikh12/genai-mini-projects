import os
import tempfile
import fitz  # PyMuPDF
import google.generativeai as genai
from dotenv import load_dotenv
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
    prompt = f"""
        You are a resume parsing assistant. Extract the following information from the resume:

        Return clean, valid JSON only — no markdown, no explanation, no code block.

        Format:
        {{
        "Full Name": "",
        "Email": "",
        "Phone Number": "",
        "Total Years of Experience": "",
        "Education": [
            {{
            "Degree": "",
            "University": "",
            "Graduation Year": ""
            }}
        ],
        "Skills": [],
        "Current Job Title": "",
        "Current Location": ""
        }}

        Resume:
        {text}
        """
    try:
        response = model.generate_content(prompt)
        cleaned = re.sub(r"```(?:json)?\n", "", response.text.strip())
        cleaned = cleaned.replace("```", "").strip()
        
        # Optional: Remove any trailing non-JSON text (just in case)
        first_brace = cleaned.find('{')
        last_brace = cleaned.rfind('}')
        json_string = cleaned[first_brace:last_brace+1]
        return json.loads(json_string)
    except Exception as e:
        return f"Error: {e}"
