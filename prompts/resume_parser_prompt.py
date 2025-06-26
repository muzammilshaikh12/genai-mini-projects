resume_parsing_prompt = """
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
