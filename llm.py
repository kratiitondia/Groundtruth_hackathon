import os
import openai
from typing import Dict, Any

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY not set in environment")
openai.api_key = OPENAI_API_KEY

CHAT_MODEL = os.getenv("OPENAI_CHAT_MODEL", "gpt-4o")

def call_chat_system(system_prompt: str, user_prompt: str, max_tokens: int = 512) -> str:
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
    resp = openai.ChatCompletion.create(
        model=CHAT_MODEL,
        messages=messages,
        max_tokens=max_tokens,
        temperature=0.0
    )
    return resp["choices"][0]["message"]["content"]
