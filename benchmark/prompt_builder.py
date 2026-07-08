def build_json_prompt(prompt: str):

    return f"""
You are an AI assistant.

Answer ONLY in valid JSON.

Use exactly this schema.

{{
    "title": "...",
    "summary": "...",
    "example": "..."
}}

Do not write markdown.

Do not use code blocks.

Prompt:

{prompt}
"""