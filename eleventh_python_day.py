"""My eleventh day practicing Python."""

import requests


def get_github_user(username):
    """Fetch GitHub user data."""

    url = f"https://api.github.com/users/{username}"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    return response.json()


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


def calculate_repository_stats(repositories):
    """Calculate repository statistics."""

    total_stars = sum(
        repo["stargazers_count"]
        for repo in repositories
    )

    total_forks = sum(
        repo["forks_count"]
        for repo in repositories
    )

    languages = {}

    for repo in repositories:
        language = repo.get("language")

        if language:
            languages[language] = (
                languages.get(language, 0) + 1
            )

    return {
        "total_repositories": len(repositories),
        "total_stars": total_stars,
        "total_forks": total_forks,
        "languages": languages,
    }


username = "ahmed-1430"

print("Python Practice Day 11")

try:
    repositories = get_user_repositories(username)

    stats = calculate_repository_stats(repositories)

    print(f"Repositories: {stats['total_repositories']}")
    print(f"Stars: {stats['total_stars']}")
    print(f"Forks: {stats['total_forks']}")

    print("\nLanguages:")

    for language, count in stats["languages"].items():
        print(f"{language}: {count}")

except requests.exceptions.RequestException as error:
    print(f"API Error: {error}")