"""My eleventh day practicing Python."""

import requests


def get_github_user(username):
    """Fetch GitHub user data."""

    url = f"https://api.github.com/users/{username}"

    response = requests.get(url)

    return response.json()


user = get_github_user("ahmed-1430")

print("Python Practice Day 11")
print(f"Name: {user.get('name')}")
print(f"Username: {user.get('login')}")
print(f"Bio: {user.get('bio')}")
print(f"Public Repositories: {user.get('public_repos')}")