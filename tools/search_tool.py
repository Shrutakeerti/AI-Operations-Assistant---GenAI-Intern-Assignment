from ddgs import DDGS

def web_search(query):
    if not query:
        return {"error": "No query provided for web_search"}

    try:
        results = []
        with DDGS() as ddgs:
            for r in ddgs.text(query, max_results=3):
                results.append({
                    "title": r['title'].replace("\n", " ").strip(),
                    "url": r['href'],
                    "body": r['body'].replace("\n", " ").replace('"', "'").strip()
                })
        return results
    except Exception as e:
        return {"error": f"web_search failed: {str(e)}"}
