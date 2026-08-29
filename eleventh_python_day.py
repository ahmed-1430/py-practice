"""My eleventh day practicing Python."""

import requests


class GitHubUser:
    """Represent a GitHub user."""

    def __init__(self, data):
        self.name = data.get("name")
        self.username = data.get("login")
        self.bio = data.get("bio")
        self.public_repos = data.get("public_repos")
        self.followers = data.get("followers")

    def display(self):
        """Display user information."""

        print("\nGitHub User Information")
        print("-" * 30)
        print(f"Name: {self.name or 'Not available'}")
        print(f"Username: {self.username}")
        print(f"Repositories: {self.public_repos}")
        print(f"Followers: {self.followers}")


def get_github_user(username):
    """Fetch GitHub user data."""

    url = f"https://api.github.com/users/{username}"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    return GitHubUser(response.json())


def get_user_repositories(username):
    """Fetch GitHub user repositories."""

    url = f"https://api.github.com/users/{username}/repos"

    response = requests.get(
        url,
        timeout=10,
    )

    response.raise_for_status()

    return response.json()


username = "ahmed-1430"

print("Python Practice Day 11")

try:
    user = get_github_user(username)
    repositories = get_user_repositories(username)

    user.display()

    print("\nRepositories:")

    for repo in repositories:
        print(f"- {repo['name']}")

except requests.exceptions.RequestException as error:
    print(f"API Error: {error}")