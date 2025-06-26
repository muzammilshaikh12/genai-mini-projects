from fastapi import APIRouter, UploadFile, File, Form
from services import jd_matcher

router = APIRouter()

@router.post("/compare-jd")
async def compare_resume_and_jd(file: UploadFile = File(...),jd_url: str = Form(...)):
    # Step 1: Extract resume text
    resume_text = jd_matcher.extract_resume_text(file)

    # Step 2: Fetch and extract JD text from LinkedIn URL
    page_text = jd_matcher.fetch_linkedin_page_text(jd_url)
    jd_text = jd_matcher.extract_jd_from_page_text(page_text)
    
    # Step 3: Compare both using Gemini and return result
    result = jd_matcher.compare_resume_to_jd(resume_text, jd_text)

    return result
