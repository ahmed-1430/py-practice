"""My eleventh day practicing Python."""

import requests


def get_user_repositories(username):
    """Fetch GitHub repositories."""

    url = f"https://api.github.com/users/{username}/repos"

    params = {
        "per_page": 100,
        "sort": "updated",
    }

    response = requests.get(
        url,
        params=params,
        timeout=10,
    )

    response.raise_for_status()

    return response.json()


def search_repositories(repositories, keyword):
    """Search repositories by name."""

    results = []

    for repo in repositories:
        if keyword.lower() in repo["name"].lower():
            results.append(repo)

    return results


username = "ahmed-1430"

print("Python Practice Day 11")

try:
    repositories = get_user_repositories(username)

    keyword = input(
        "Search repository: "
    ).strip()

    results = search_repositories(
        repositories,
        keyword,
    )

    if results:
        print("\nRepositories Found:")

        for repo in results:
            print(
                f"- {repo['name']} "
                f"⭐ {repo['stargazers_count']}"
            )
    else:
        print("No repositories found.")

except requests.exceptions.RequestException as error:
    print(f"API Error: {error}")