"""My thirteenth day practicing Python."""

from datetime import datetime
from functools import wraps


class TaskManager:
    """Manage and process tasks."""

    def __init__(self):
        self.tasks = []
        self.completed_tasks = []

    def add_task(self, title, priority="Medium"):
        """Add a new task."""

        task = {
            "id": len(self.tasks) + 1,
            "title": title.strip(),
            "priority": priority.title(),
            "status": "Pending",
            "created_at": datetime.now().strftime(
                "%Y-%m-%d %H:%M"
            ),
        }

        self.tasks.append(task)

        return task

    def generate_pending_tasks(self):
        """Generate pending tasks one by one."""

        for task in self.tasks:
            if task["status"] == "Pending":
                yield task

    def show_tasks(self):
        """Display all tasks."""

        if not self.tasks:
            print("\nNo tasks found.")
            return

        print("\n" + "=" * 45)
        print("TASK LIST")
        print("=" * 45)

        for task in self.tasks:
            print(
                f"{task['id']}. "
                f"{task['title']}"
            )

            print(
                f"   Priority: "
                f"{task['priority']}"
            )

            print(
                f"   Status: "
                f"{task['status']}"
            )


def log_processing(func):
    """Log task processing."""

    @wraps(func)
    def wrapper(self, task):
        start_time = datetime.now()

        print("\n" + "-" * 45)
        print(
            f"Processing task: "
            f"{task['title']}"
        )

        result = func(self, task)

        end_time = datetime.now()

        duration = (
            end_time - start_time
        ).total_seconds()

        print(
            f"Completed in "
            f"{duration:.2f} seconds"
        )

        print("-" * 45)

        return result

    return wrapper


class TaskProcessor:
    """Process tasks."""

    def __init__(self, manager):
        self.manager = manager

    @log_processing
    def process_task(self, task):
        """Mark a task as completed."""

        task["status"] = "Completed"

        task["completed_at"] = (
            datetime.now().strftime(
                "%Y-%m-%d %H:%M"
            )
        )

        self.manager.completed_tasks.append(
            task
        )

        return task

    def process_all_tasks(self):
        """Process all pending tasks."""

        pending_tasks = list(
            self.manager.generate_pending_tasks()
        )

        if not pending_tasks:
            print("\nNo pending tasks to process.")
            return

        for task in pending_tasks:
            self.process_task(task)


def main():
    """Run the task processing system."""

    print("=" * 45)
    print("   PYTHON TASK PROCESSING SYSTEM")
    print("         PRACTICE DAY 13")
    print("=" * 45)

    manager = TaskManager()
    processor = TaskProcessor(manager)

    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Process All Tasks")
        print("4. View Completed Tasks")
        print("5. Exit")

        choice = input(
            "\nChoose an option: "
        ).strip()

        if choice == "1":
            title = input(
                "Enter task title: "
            ).strip()

            priority = input(
                "Enter priority "
                "(Low/Medium/High): "
            ).strip()

            if not title:
                print(
                    "Task title cannot be empty."
                )
                continue

            if not priority:
                priority = "Medium"

            manager.add_task(
                title,
                priority,
            )

            print(
                "Task added successfully."
            )

        elif choice == "2":
            manager.show_tasks()

        elif choice == "3":
            processor.process_all_tasks()

        elif choice == "4":
            if not manager.completed_tasks:
                print(
                    "\nNo completed tasks found."
                )

            else:
                print(
                    "\nCOMPLETED TASKS"
                )

                for task in (
                    manager.completed_tasks
                ):
                    print(
                        f"- {task['title']}"
                    )

                    print(
                        f"  Completed: "
                        f"{task['completed_at']}"
                    )

        elif choice == "5":
            print(
                "\nThanks for practicing Python!"
            )
            break

        else:
            print(
                "Invalid option. Try again."
            )


if __name__ == "__main__":
    main()