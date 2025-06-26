import json
import re

def extract_clean_json(text: str) -> dict:
    """
    Cleans markdown-wrapped JSON like:
    ```json
    { ... }
    ```
    and returns a proper Python dictionary.
    """
    # Remove Markdown formatting like ```json and ```
    cleaned = re.sub(r"```(?:json)?\n", "", text.strip())
    cleaned = cleaned.replace("```", "").strip()

    # Find first and last brace to isolate JSON block
    first_brace = cleaned.find('{')
    last_brace = cleaned.rfind('}')
    json_string = cleaned[first_brace:last_brace + 1]

    return json.loads(json_string)
