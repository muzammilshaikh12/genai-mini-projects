from fastapi import APIRouter, UploadFile, File
from services.resume_parser import extract_text_from_pdf, parse_resume_from_text

router = APIRouter()

@router.post("/parse-resume")
async def parse_resume(file: UploadFile = File(...)):
    file_bytes = await file.read()
    resume_text = extract_text_from_pdf(file_bytes)
    parsed_info = parse_resume_from_text(resume_text)
    return {"parsed_resume": parsed_info}
