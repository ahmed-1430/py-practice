"""My twelfth day practicing Python."""

import asyncio

import aiohttp


async def get_repositories(
    session,
    username,
):
    """Fetch repositories."""

    url = (
        f"https://api.github.com/"
        f"users/{username}/repos"
    )

    params = {
        "per_page": 100,
    }

    async with session.get(
        url,
        params=params,
    ) as response:
        if response.status != 200:
            return []

        return await response.json()


def calculate_stats(repositories):
    """Calculate repository statistics."""

    total_stars = sum(
        repo.get(
            "stargazers_count",
            0,
        )
        for repo in repositories
    )

    total_forks = sum(
        repo.get(
            "forks_count",
            0,
        )
        for repo in repositories
    )

    languages = {}

    for repo in repositories:
        language = repo.get("language")

        if language:
            languages[language] = (
                languages.get(language, 0)
                + 1
            )

    return {
        "repositories": len(repositories),
        "stars": total_stars,
        "forks": total_forks,
        "languages": languages,
    }


async def main():
    """Run the application."""

    username = "ahmed-1430"

    async with aiohttp.ClientSession() as session:

        repositories = await get_repositories(
            session,
            username,
        )

        stats = calculate_stats(
            repositories
        )

        print("Python Practice Day 12")

        print(
            f"Repositories: "
            f"{stats['repositories']}"
        )

        print(
            f"Stars: "
            f"{stats['stars']}"
        )

        print(
            f"Forks: "
            f"{stats['forks']}"
        )

        print("\nLanguages:")

        for language, count in (
            stats["languages"].items()
        ):
            print(
                f"{language}: {count}"
            )


asyncio.run(main())