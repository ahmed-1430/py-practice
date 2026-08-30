"""My twelfth day practicing Python."""

import asyncio

import aiohttp


class GitHubUser:
    """Represent GitHub user information."""

    def __init__(self, data):
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

    def display(self):
        """Display user information."""

        print(
            f"\nUsername: {self.username}"
        )

        print(
            f"Name: "
            f"{self.name or 'Not available'}"
        )

        print(
            f"Followers: {self.followers}"
        )

        print(
            f"Public Repositories: "
            f"{self.public_repos}"
        )


async def get_github_user(
    session,
    username,
):
    """Fetch a GitHub user."""

    url = (
        f"https://api.github.com/"
        f"users/{username}"
    )

    try:
        async with session.get(url) as response:
            if response.status != 200:
                return None

            data = await response.json()

            return GitHubUser(data)

    except aiohttp.ClientError:
        return None


async def main():
    """Run the application."""

    usernames = [
        "ahmed-1430",
        "torvalds",
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [
            get_github_user(
                session,
                username,
            )
            for username in usernames
        ]

        users = await asyncio.gather(*tasks)

        print("Python Practice Day 12")

        for user in users:
            if user:
                user.display()


asyncio.run(main())