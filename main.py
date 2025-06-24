# app/main.py
from fastapi import FastAPI
from routers import summarizer, gemini_chat

app = FastAPI(
    title="GenAI Mini Projects API",
    version="1.0.0",
    description="A collection of GenAI-powered tools using Gemini and FastAPI."
)

# Route registrations
app.include_router(summarizer.router, prefix="/summarize", tags=["Summarizer"])
app.include_router(gemini_chat.router, prefix="/chat", tags=["Chat"])

@app.get("/")
async def root():
    return {"message": "Welcome to the GenAI Mini Projects API 🚀"}
