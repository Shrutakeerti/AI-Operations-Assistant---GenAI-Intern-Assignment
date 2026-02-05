import os
import requests

def news_search(query):

    key = os.getenv("NEWS_API_KEY")

    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={key}"

    r = requests.get(url)
    data = r.json()

    articles = []

    for a in data["articles"][:3]:
        articles.append({
            "title": a["title"],
            "source": a["source"]["name"],
            "url": a["url"]
        })

    return articles
