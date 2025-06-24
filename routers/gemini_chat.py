# app/routers/gemini_chat.py
from fastapi import APIRouter
from services.gemini_utils import generate_gemini_response

router = APIRouter()

@router.post("/")
def chat_with_gemini(prompt: str):
    return {"response": generate_gemini_response(prompt)}
