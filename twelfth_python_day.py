"""My twelfth day practicing Python."""

import asyncio

import aiohttp


class GitHubUser:
    """Represent GitHub user information."""

    def __init__(
        self,
        data,
        repositories=None,
    ):
        self.username = data.get("login")
        self.name = data.get("name")
        self.followers = data.get(
            "followers",
            0,
        )
        self.public_repos = data.get(
            "public_repos",
            0,
        )
        self.repositories = repositories or []

    def repository_stats(self):
        """Calculate repository statistics."""

        total_stars = sum(
            repo.get(
                "stargazers_count",
                0,
            )
            for repo in self.repositories
        )

        total_forks = sum(
            repo.get(
                "forks_count",
                0,
            )
            for repo in self.repositories
        )

        languages = {}

        for repo in self.repositories:
            language = repo.get("language")

            if language:
                languages[language] = (
                    languages.get(
                        language,
                        0,
                    )
                    + 1
                )

        return {
            "total_repositories": len(
                self.repositories
            ),
            "total_stars": total_stars,
            "total_forks": total_forks,
            "languages": languages,
        }

    def display(self):
        """Display user analysis."""

        stats = self.repository_stats()

        print("\n" + "=" * 40)
        print(
            f"GITHUB USER: "
            f"{self.username}"
        )
        print("=" * 40)

        print(
            f"Name: "
            f"{self.name or 'Not available'}"
        )

        print(
            f"Followers: "
            f"{self.followers}"
        )

        print(
            f"Public Repositories: "
            f"{self.public_repos}"
        )

        print("\nRepository Statistics")

        print(
            f"Repositories Analyzed: "
            f"{stats['total_repositories']}"
        )

        print(
            f"Total Stars: "
            f"{stats['total_stars']}"
        )

        print(
            f"Total Forks: "
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
                print(
                    f"- {language}: "
                    f"{count}"
                )


class AsyncGitHubAnalyzer:
    """Fetch and analyze GitHub data asynchronously."""

    BASE_URL = "https://api.github.com"

    def __init__(self, session):
        self.session = session

    async def get_user(self, username):
        """Fetch GitHub user data."""

        url = (
            f"{self.BASE_URL}/"
            f"users/{username}"
        )

        try:
            async with self.session.get(
                url
            ) as response:

                if response.status == 404:
                    print(
                        f"User '{username}' "
                        f"not found."
                    )
                    return None

                if response.status != 200:
                    print(
                        f"Could not fetch "
                        f"{username}. "
                        f"Status: "
                        f"{response.status}"
                    )
                    return None

                return await response.json()

        except aiohttp.ClientError as error:
            print(
                f"Request error for "
                f"{username}: {error}"
            )
            return None

    async def get_repositories(
        self,
        username,
    ):
        """Fetch user repositories."""

        url = (
            f"{self.BASE_URL}/"
            f"users/{username}/repos"
        )

        params = {
            "per_page": 100,
            "sort": "updated",
        }

        try:
            async with self.session.get(
                url,
                params=params,
            ) as response:

                if response.status != 200:
                    return []

                return await response.json()

        except aiohttp.ClientError:
            return []

    async def analyze_user(
        self,
        username,
    ):
        """Fetch and analyze one user concurrently."""

        user_task = self.get_user(
            username
        )

        repositories_task = (
            self.get_repositories(
                username
            )
        )

        user_data, repositories = (
            await asyncio.gather(
                user_task,
                repositories_task,
            )
        )

        if not user_data:
            return None

        return GitHubUser(
            user_data,
            repositories,
        )


async def main():
    """Run the async GitHub analyzer."""

    print("=" * 45)
    print(" ASYNC GITHUB PROFILE ANALYZER")
    print("      PYTHON PRACTICE DAY 12")
    print("=" * 45)

    usernames = input(
        "\nEnter GitHub usernames "
        "(separated by commas): "
    ).strip()

    if not usernames:
        print("Please enter at least one username.")
        return

    username_list = [
        username.strip()
        for username in usernames.split(",")
        if username.strip()
    ]

    timeout = aiohttp.ClientTimeout(
        total=15
    )

    async with aiohttp.ClientSession(
        timeout=timeout
    ) as session:

        analyzer = AsyncGitHubAnalyzer(
            session
        )

        tasks = [
            analyzer.analyze_user(
                username
            )
            for username in username_list
        ]

        results = await asyncio.gather(
            *tasks
        )

        users = [
            user
            for user in results
            if user
        ]

        if not users:
            print(
                "\nNo user data could "
                "be fetched."
            )
            return

        print(
            f"\nSuccessfully analyzed "
            f"{len(users)} user(s)."
        )

        for user in users:
            user.display()


if __name__ == "__main__":
    asyncio.run(main())