"""My fourth day practicing Python."""


def add_task(tasks, title):
    """Add a new unfinished task to a task list."""
    tasks.append({"title": title, "complete": False})


def show_tasks(tasks):
    """Print every task with its current status."""
    for task in tasks:
        status = "done" if task["complete"] else "to do"
        print(f"- {task['title']} ({status})")


def mark_task_complete(tasks, title):
    """Mark a task complete and report whether it was found."""
    for task in tasks:
        if task["title"] == title:
            task["complete"] = True
            return True
    return False


print("Welcome to Python practice day 4!")
print("Today I am building a small task-list program.")

my_tasks = []
add_task(my_tasks, "Read Python notes")
add_task(my_tasks, "Write a practice program")

print("My tasks for today:")
show_tasks(my_tasks)

mark_task_complete(my_tasks, "Read Python notes")
print("\nAfter completing one task:")
show_tasks(my_tasks)
