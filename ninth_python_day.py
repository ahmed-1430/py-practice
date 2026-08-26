"""My ninth day practicing Python."""

import json
from datetime import datetime


DATA_FILE = "expenses.json"


def load_expenses():
    """Load expenses from JSON."""

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Warning: expense data is corrupted.")
        return []


def save_expenses(expenses):
    """Save expenses to JSON."""

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses, title, amount, category):
    """Add a new expense."""

    if not title.strip():
        print("Title cannot be empty.")
        return False

    if amount <= 0:
        print("Amount must be greater than zero.")
        return False

    if not category.strip():
        print("Category cannot be empty.")
        return False

    expense = {
        "title": title.strip(),
        "amount": amount,
        "category": category.strip().title(),
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }

    expenses.append(expense)

    return True


def calculate_total(expenses):
    """Calculate total expenses."""

    return sum(expense["amount"] for expense in expenses)


def category_summary(expenses):
    """Calculate spending by category."""

    summary = {}

    for expense in expenses:
        category = expense["category"]

        summary[category] = (
            summary.get(category, 0)
            + expense["amount"]
        )

    return summary


def show_expenses(expenses):
    """Display all expenses."""

    if not expenses:
        print("\nNo expenses found.")
        return

    print("\nExpense History")
    print("-" * 60)

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. "
            f"{expense['date']} | "
            f"{expense['title']} | "
            f"{expense['category']} | "
            f"{expense['amount']:.2f} BDT"
        )


def show_summary(expenses):
    """Display expense statistics."""

    total = calculate_total(expenses)
    summary = category_summary(expenses)

    print("\nExpense Summary")
    print("-" * 30)
    print(f"Total spent: {total:.2f} BDT")

    print("\nBy Category:")

    if not summary:
        print("No category data available.")
        return

    for category, amount in summary.items():
        print(f"{category}: {amount:.2f} BDT")


def get_amount():
    """Get a valid amount from the user."""

    while True:
        try:
            amount = float(input("Amount: "))

            if amount <= 0:
                print("Amount must be greater than zero.")
                continue

            return amount

        except ValueError:
            print("Please enter a valid number.")


def main():
    """Run the expense tracker."""

    print("=" * 40)
    print("      PYTHON EXPENSE TRACKER")
    print("          Practice Day 9")
    print("=" * 40)

    expenses = load_expenses()

    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. View Summary")
        print("4. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            title = input("Title: ").strip()
            category = input("Category: ").strip()
            amount = get_amount()

            if add_expense(
                expenses,
                title,
                amount,
                category,
            ):
                save_expenses(expenses)
                print("Expense added successfully.")

        elif choice == "2":
            show_expenses(expenses)

        elif choice == "3":
            show_summary(expenses)

        elif choice == "4":
            save_expenses(expenses)
            print("Data saved. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()