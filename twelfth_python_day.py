"""My twelfth day practicing Python."""

import asyncio

import aiohttp


async def get_github_user(
    session,
    username,
):
    """Fetch GitHub user."""

    url = (
        f"https://api.github.com/"
        f"users/{username}"
    )

    try:
        async with session.get(url) as response:
            if response.status != 200:
                return None

            return await response.json()

    except aiohttp.ClientError:
        return None


async def analyze_user(
    session,
    username,
):
    """Analyze a GitHub user."""

    user = await get_github_user(
        session,
        username,
    )

    if not user:
        return None

    return {
        "username": user.get("login"),
        "followers": user.get(
            "followers",
            0,
        ),
        "repositories": user.get(
            "public_repos",
            0,
        ),
    }


async def main():
    """Analyze users concurrently."""

    usernames = [
        "ahmed-1430",
        "torvalds",
        "octocat",
    ]

    async with aiohttp.ClientSession() as session:

        tasks = [
            analyze_user(
                session,
                username,
            )
            for username in usernames
        ]

        results = await asyncio.gather(
            *tasks
        )

        print("Python Practice Day 12")
        print("\nGitHub User Comparison")

        for user in results:
            if user:
                print(
                    f"\n{user['username']}"
                )

                print(
                    f"Followers: "
                    f"{user['followers']}"
                )

                print(
                    f"Repositories: "
                    f"{user['repositories']}"
                )


asyncio.run(main())