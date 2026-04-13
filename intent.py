# intent.py
import requests
import json

def classify_intent(text):
    prompt = f"""
    Classify the user's intent into one of:
    - create_file
    - write_code
    - summarize
    - chat

    Also extract details if needed.

    User input: "{text}"

    Return JSON:
    {{
        "intent": "...",
        "details": "..."
    }}
    """

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "mistral", "prompt": prompt}
    )

    output = response.json()["response"]

    try:
        return json.loads(output)
    except:
        return {"intent": "chat", "details": text}