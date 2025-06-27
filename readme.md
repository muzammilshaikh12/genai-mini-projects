# 🤖 GenAI Mini Projects – Powered by Gemini

Welcome to the **GenAI Mini Projects** repository!  
This is a hands-on collection of AI-powered microservices and APIs built using **Google Gemini**, **FastAPI**, and supporting tools like PyMuPDF, httpx, and more.

---

## 📦 What’s Inside

Each project is a standalone API (1–3 functions) with clean separation of logic, prompts, and utilities.

| Project                  | Description                                                  |
|--------------------------|--------------------------------------------------------------|
| 📝 Text Summarizer       | Summarizes plain text using Gemini                          |
| 📄 PDF Summarizer        | Extracts and summarizes PDF contents                        |
| 🎯 Resume Parser         | Extracts structured data (name, skills, education, etc.) from resume PDF |
| 🔍 JD Matcher            | Compares resume vs LinkedIn JD and gives match percentage and recommendation |
| 🧹 JSON Cleaner          | Utility to clean messy LLM output into valid JSON           |
| ✨ More coming soon       | RAG, chatbot memory, agents, semantic search, and more      |

---

## 🚀 How to Run

1. Clone the repo

git clone https://github.com/muzammilshaikh12/genai-mini-projects.git
cd genai-mini-projects

2. Install dependencies

pip install -r requirements.txt

3. Set up your Gemini API key

Create a `.env` file in the root with the following content:

GEMINI_API_KEY=your_google_genai_api_key

4. Start the FastAPI server

uvicorn main:app --reload

5. Open Swagger UI

Visit: http://localhost:8000/docs

---

## 🧠 Tech Stack

- LLM: Google Gemini (via `google-generativeai`)
- Framework: FastAPI + Uvicorn
- PDF Parsing: PyMuPDF
- Web Scraping: httpx + BeautifulSoup
- Prompt Design: Modular prompt templates per feature

---

## 🗂️ Project Structure

genai-mini-projects/
├── main.py  
├── routers/  
│   ├── summarizer.py  
│   ├── resume_parser.py  
│   └── jd_matcher.py  
├── services/  
│   ├── summarizer_logic.py  
│   ├── resume_parser.py  
│   └── jd_matcher.py  
├── prompts/  
│   ├── resume__parser_prompts.py  
│   └── jd_prompts.py  
├── utils/  
│   └── json_cleaner.py  
├── requirements.txt  
└── .env

---

## 🛠 Planned Additions

- ✅ Agentic AI (after bootcamp)
- ✅ MCP Toolbox integration
- ✅ Semantic Search + Vector DB (e.g., FAISS, ChromaDB)
- ✅ Chat memory with context windows
- ✅ LangChain & RAG experiments

---

## ✍️ Author

**Muzammil Shaikh**  
Backend Developer · GenAI Explorer  
Crafting smart tools with clean APIs and LLMs ⚙️🧠

---

## 📜 License

MIT – use it freely and share your creations!
