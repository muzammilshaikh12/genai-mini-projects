# app/services/summarizer_logic.py
import google.generativeai as genai
import os
import fitz
import tempfile
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(
    "gemini-1.5-flash",
    generation_config=genai.types.GenerationConfig(
        temperature=0.3,
        top_k=20,
        top_p=0.8,
        max_output_tokens=512
    )
)

def generate_summary(text: str) -> str:
    prompt = f"Summarize this text in simple terms:\n\n{text}"
    response = model.generate_content(prompt)
    return response.text.strip()

def extract_text_from_pdf(uploaded_file) -> str:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file)
        tmp_path = tmp.name

    doc = fitz.open(tmp_path)
    full_text = ""
    for page in doc:
        full_text += page.get_text() + "\n"
    doc.close()
    os.remove(tmp_path)
    return full_text.strip()

def summarize_text_with_gemini(full_text: str) -> str:
    words = full_text.split()
    chunk_size = 500
    chunks = [" ".join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]
    summaries = []
    instruction = (
        "You are a professional document summarizer. "
        "Read the given text and provide a concise, clear summary highlighting key points."
    )
    for chunk in chunks:
        try:
            response = model.generate_content(f"{instruction}\n\n{chunk}")
            summaries.append(response.text.strip())
        except Exception as e:
            summaries.append(f"[Error summarizing chunk]: {e}")

    return "\n\n".join(summaries)
