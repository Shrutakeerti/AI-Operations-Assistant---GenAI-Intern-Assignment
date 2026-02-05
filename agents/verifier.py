import json
import re
from llm.groq_client import call_llm

class VerifierAgent:

    def repair_json(self, text):
        # Locate the first '{' and the last '}'
        start = text.find("{")
        end = text.rfind("}")

        if start == -1 or end == -1:
            # Fallback: return a valid empty schema so the app doesn't crash
            print(f"⚠️ Verifier failed to generate JSON. Raw output:\n{text}")
            return {"github": [], "news": [], "search_results": []}

        j = text[start : end + 1]

        # Common LLM fixes
        j = j.replace("}}]", "}]")
        j = j.replace(",]", "]")
        j = j.replace(",}", "}")

        try:
            return json.loads(j)
        except json.JSONDecodeError:
            print(f"⚠️ JSON Decode Error. Raw trimmed:\n{j}")
            # Fallback
            return {"github": [], "news": [], "search_results": []}

    def verify(self, raw_results):

        prompt = f"""
Return ONLY JSON.

Schema:

{{
 "github":[{{"name":"","stars":0,"url":"","description":""}}],
 "news":[{{"title":"","source":"","url":""}}],
 "search_results":[{{"title":"","url":"","body":""}}]
}}

Strict JSON. Escape quotes in strings.

NO explanation.

Data:
{raw_results}
"""

        result = call_llm(prompt)

        print("\n🧪 RAW VERIFIER OUTPUT:\n", result)

        return self.repair_json(result)
