"""My eleventh day practicing Python."""

import requests


class GitHubUser:
    """Represent a GitHub user."""

    def __init__(self, data):
        self.name = data.get("name")
        self.username = data.get("login")
        self.bio = data.get("bio")
        self.public_repos = data.get("public_repos", 0)
        self.followers = data.get("followers", 0)
        self.following = data.get("following", 0)
        self.location = data.get("location")

    def display(self):
        """Display GitHub user information."""

        print("\n" + "=" * 40)
        print("GITHUB USER PROFILE")
        print("=" * 40)

        print(f"Name: {self.name or 'Not available'}")
        print(f"Username: {self.username}")
        print(f"Bio: {self.bio or 'Not available'}")
        print(f"Location: {self.location or 'Not available'}")
        print(f"Public Repositories: {self.public_repos}")
        print(f"Followers: {self.followers}")
        print(f"Following: {self.following}")


class GitHubAnalyzer:
    """Fetch and analyze GitHub user data."""

    BASE_URL = "https://api.github.com"

    def get_user(self, username):
        """Fetch GitHub user data."""

        url = f"{self.BASE_URL}/users/{username}"

        response = requests.get(
            url,
            timeout=10,
        )

        response.raise_for_status()

        return GitHubUser(response.json())

    def get_repositories(self, username):
        """Fetch GitHub user repositories."""

        url = (
            f"{self.BASE_URL}/users/"
            f"{username}/repos"
        )

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

    def calculate_stats(self, repositories):
        """Calculate repository statistics."""

        total_stars = sum(
            repo.get("stargazers_count", 0)
            for repo in repositories
        )

        total_forks = sum(
            repo.get("forks_count", 0)
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

    def search_repositories(
        self,
        repositories,
        keyword,
    ):
        """Search repositories by keyword."""

        return [
            repo
            for repo in repositories
            if keyword.lower()
            in repo["name"].lower()
        ]

    def display_statistics(self, stats):
        """Display repository statistics."""

        print("\n" + "=" * 40)
        print("REPOSITORY STATISTICS")
        print("=" * 40)

        print(
            f"Repositories analyzed: "
            f"{stats['total_repositories']}"
        )

        print(
            f"Total stars: "
            f"{stats['total_stars']}"
        )

        print(
            f"Total forks: "
            f"{stats['total_forks']}"
        )

        print("\nLanguages:")

        if not stats["languages"]:
            print("No language data found.")

        else:
            for language, count in sorted(
                stats["languages"].items(),
                key=lambda item: item[1],
                reverse=True,
            ):
                print(f"- {language}: {count}")


def main():
    """Run the GitHub Profile Analyzer."""

    print("=" * 40)
    print("  GITHUB PROFILE ANALYZER")
    print("     PYTHON PRACTICE DAY 11")
    print("=" * 40)

    username = input(
        "\nEnter GitHub username: "
    ).strip()

    if not username:
        print("Username cannot be empty.")
        return

    analyzer = GitHubAnalyzer()

    try:
        user = analyzer.get_user(username)
        repositories = analyzer.get_repositories(
            username
        )

        user.display()

        stats = analyzer.calculate_stats(
            repositories
        )

        analyzer.display_statistics(stats)

        keyword = input(
            "\nSearch repositories "
            "(press Enter to skip): "
        ).strip()

        if keyword:
            results = analyzer.search_repositories(
                repositories,
                keyword,
            )

            print("\nSEARCH RESULTS")

            if not results:
                print("No repositories found.")

            else:
                for repo in results:
                    print(
                        f"- {repo['name']} "
                        f"⭐ {repo.get('stargazers_count', 0)}"
                    )

    except requests.exceptions.HTTPError as error:
        if error.response.status_code == 404:
            print("GitHub user not found.")
        else:
            print(
                f"GitHub API error: "
                f"{error.response.status_code}"
            )

    except requests.exceptions.ConnectionError:
        print("Internet connection error.")

    except requests.exceptions.Timeout:
        print("Request timed out.")

    except requests.exceptions.RequestException as error:
        print(f"Request error: {error}")


if __name__ == "__main__":
    main()