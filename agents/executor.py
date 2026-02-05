from tools.github_tool import github_search
from tools.news_tool import news_search
from tools.search_tool import web_search

class ExecutorAgent:

    def execute(self, plan):

        results = []
        discovered_urls = []

        for step in plan["steps"]:
            tool = step["tool"]
            inp = step["input"]

            if tool == "github_search":
                results.append(github_search(inp))

            elif tool == "news_search":
                results.append(news_search(inp))

            elif tool == "web_search":
                res = web_search(inp)
                results.append(res)
                if isinstance(res, list):
                    discovered_urls.extend([r["url"] for r in res if "url" in r])

        return results
