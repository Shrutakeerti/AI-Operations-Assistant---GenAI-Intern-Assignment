import json
import re
from llm.groq_client import call_llm

class PlannerAgent:

    def extract_json(self, text):
        match = re.search(r"\{[\s\S]*\}", text)
        if not match:
            raise RuntimeError("Planner did not return JSON:\n" + text)
        return json.loads(match.group())

    def plan(self, user_task):

        prompt = f"""
Return ONLY JSON.

Schema:
{{"steps":[{{"tool":"github_search","input":""}},{{"tool":"news_search","input":""}},{{"tool":"web_search","input":""}}]}}

Tools:
- github_search: for finding repositories.
- news_search: for finding news articles.
- web_search: for general knowledge, facts, and finding websites.

Task:
{user_task}
"""


        result = call_llm(prompt)

        print("\n🧪 RAW PLANNER OUTPUT:\n", result)

        return self.extract_json(result)
