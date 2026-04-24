import json
import re

def parse_llm_response(content):
    try:
        # Pastikan content adalah string
        if isinstance(content, dict):
            content = content.get("response", "")

        # Hapus markdown code block jika ada
        content = re.sub(r"```json\s*|\s*```", "", content)
        content = content.strip()

        parsed = json.loads(content)
        return parsed.get("motivations", [])

    except Exception as e:
        raise Exception(f"Invalid JSON from LLM: {str(e)}")