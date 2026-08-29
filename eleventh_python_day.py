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
        self.following = data.get("following")

    def display(self):
        """Display user information."""

        print("\nGitHub User Information")
        print("-" * 30)
        print(f"Name: {self.name or 'Not available'}")
        print(f"Username: {self.username}")
        print(f"Bio: {self.bio or 'Not available'}")
        print(f"Repositories: {self.public_repos}")
        print(f"Followers: {self.followers}")
        print(f"Following: {self.following}")


def get_github_user(username):
    """Fetch GitHub user data."""

    url = f"https://api.github.com/users/{username}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        return GitHubUser(response.json())

    except requests.exceptions.RequestException as error:
        print(f"Error: {error}")
        return None


user = get_github_user("ahmed-1430")

print("Python Practice Day 11")

if user:
    user.display()