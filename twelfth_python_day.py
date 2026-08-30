"""My twelfth day practicing Python."""

import asyncio


async def task(name, delay):
    """Run an async task."""

    print(f"{name} started.")

    await asyncio.sleep(delay)

    print(f"{name} completed.")


async def main():
    """Run multiple tasks concurrently."""

    await asyncio.gather(
        task("Task One", 3),
        task("Task Two", 2),
        task("Task Three", 1),
    )


asyncio.run(main())