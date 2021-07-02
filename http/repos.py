import requests

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"


class RepoData:
    r = requests.get(url)
    if r.status_code == 200:
        response = r.json()
        print(response.keys())
    else:
        print(f"Code:{r.status_code}")


if __name__ == "__main__":
    rep = RepoData()
