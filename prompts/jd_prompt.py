# prompts/jd_prompts.py

# Used to extract only JD content from full LinkedIn job page
jd_extraction_prompt = """
You're given the raw page text of a LinkedIn job posting.

✅ Your task:
Extract only the **Job Description** portion.
Ignore headers, footers, navigation, or company descriptions.

--- PAGE TEXT START ---
{page_text}
--- PAGE TEXT END ---

Output only plain job description text.
"""

# Used to compare Resume with JD and generate structured feedback
jd_comparison_prompt = """
Compare the following Resume and Job Description.

Resume:
{resume}

Job Description:
{jd}

✅ Now return JSON with:
- match_percentage (0-100)
- matched_skills (list)
- missing_skills (list)
- feedback (1-line advice for improvement)
- apply_recommendation ("Yes" or "No")

🎯 Recommendation Logic:
- If match_percentage >= 70 → apply_recommendation: "Yes"
- Else → apply_recommendation: "No"

✅ JSON format:
{{
  "match_percentage": 84,
  "matched_skills": ["Python", "SQL"],
  "missing_skills": ["Docker", "LangChain"],
  "feedback": "Learn Docker and LangChain to boost alignment.",
  "apply_recommendation": "Yes"
}}

Only return valid JSON. No markdown, no extra text.
"""

