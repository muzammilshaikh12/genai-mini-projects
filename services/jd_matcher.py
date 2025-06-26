import fitz  # PyMuPDF
import httpx
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import google.generativeai as genai
import os 
from prompts.jd_prompt import jd_extraction_prompt, jd_comparison_prompt
from utils.json_cleaner import extract_clean_json

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=genai.types.GenerationConfig(
        temperature=0.2,       
        top_k=20,             
        top_p=0.8,             
        max_output_tokens=512 
    )
)

# 1. Extract resume text using PyMuPDF
def extract_resume_text(file) -> str:
    doc = fitz.open(stream=file.file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text.strip()

# 2. Fetch full text content from LinkedIn job post page
def fetch_linkedin_page_text(url: str) -> str:
    headers = {"User-Agent": "Mozilla/5.0"}
    res = httpx.get(url, headers=headers, timeout=10)
    return BeautifulSoup(res.text, "html.parser").get_text()

# 3. Use Gemini to extract just the Job Description portion
def extract_jd_from_page_text(page_text: str) -> str:
    prompt = jd_extraction_prompt.format(page_text=page_text)
    response = model.generate_content(prompt)
    return response.text.strip()

# 4. Compare resume to JD using Gemini with JSON output
def compare_resume_to_jd(resume_text: str, jd_text: str) -> dict:
    prompt = jd_comparison_prompt.format(resume=resume_text, jd=jd_text)
    response = model.generate_content(prompt)
    return extract_clean_json(response.text)
