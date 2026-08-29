"""My eleventh day practicing Python."""

import requests


def get_github_user(username):
    """Fetch GitHub user data."""

    url = f"https://api.github.com/users/{username}"

    response = requests.get(url)

    if response.status_code == 404:
        print("GitHub user not found.")
        return None

    return response.json()


username = "ahmed-1430"

user = get_github_user(username)

print("Python Practice Day 11")

if user:
    print(f"Name: {user.get('name')}")
    print(f"Username: {user.get('login')}")
    print(f"Public Repositories: {user.get('public_repos')}")