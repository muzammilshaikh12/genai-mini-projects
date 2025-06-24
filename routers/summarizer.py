# app/routers/summarizer.py
from fastapi import APIRouter, UploadFile, File
from services.summarizer_logic import generate_summary, extract_text_from_pdf, summarize_text_with_gemini

router = APIRouter()

@router.post("/text")
async def summarize_text(text: str):
    return {"summary": generate_summary(text)}

@router.post("/pdf")
async def summarize_pdf(file: UploadFile = File(...)):
    contents = await file.read()
    full_text = extract_text_from_pdf(contents)
    summary = summarize_text_with_gemini(full_text)
    return {"summary": summary}
