"""My thirteenth day practicing Python."""

from datetime import datetime


tasks = [
    {
        "title": "Learn Generators",
        "priority": "High",
    },
    {
        "title": "Practice Decorators",
        "priority": "High",
    },
    {
        "title": "Build Python Project",
        "priority": "Medium",
    },
]


def generate_tasks(task_list):
    """Generate tasks one at a time."""

    for task in task_list:
        yield task


def log_task(func):
    """Log task processing time."""

    def wrapper(task):
        print("\n" + "-" * 35)

        print(
            f"Started: "
            f"{datetime.now():%H:%M:%S}"
        )

        result = func(task)

        print(
            f"Finished: "
            f"{datetime.now():%H:%M:%S}"
        )

        return result

    return wrapper


@log_task
def process_task(task):
    """Process a task."""

    print(
        f"Processing: "
        f"{task['title']}"
    )

    print(
        f"Priority: "
        f"{task['priority']}"
    )

    return {
        **task,
        "status": "Completed",
    }


print("Python Practice Day 13")

completed_tasks = []

for task in generate_tasks(tasks):
    result = process_task(task)
    completed_tasks.append(result)


print("\nCompleted Tasks:")

for task in completed_tasks:
    print(
        f"- {task['title']} "
        f"({task['status']})"
    )