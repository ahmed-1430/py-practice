"""My thirteenth day practicing Python."""


tasks = [
    "Learn Python",
    "Practice Functions",
    "Build a Project",
    "Push Code to GitHub",
]


def generate_tasks(task_list):
    """Generate tasks one by one."""

    for task in task_list:
        yield task


print("Python Practice Day 13")
print("\nTasks:")

for task in generate_tasks(tasks):
    print(f"- {task}")