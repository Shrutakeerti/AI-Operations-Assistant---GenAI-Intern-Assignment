import requests

def github_search(query):

    url = f"https://api.github.com/search/repositories?q={query}&sort=stars"

    r = requests.get(url)
    data = r.json()

    repos = []

    for repo in data["items"][:3]:
        repos.append({
            "name": repo["full_name"],
            "stars": repo["stargazers_count"],
            "url": repo["html_url"],
            "description": repo["description"]
        })

    return repos
