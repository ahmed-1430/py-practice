"""My ninth day practicing Python."""

import json


DATA_FILE = "expenses.json"


def load_expenses():
    """Load expenses from JSON."""

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Expense file is corrupted.")
        return []


def save_expenses(expenses):
    """Save expenses to JSON."""

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses, title, amount, category):
    """Add a new expense."""

    expense = {
        "title": title,
        "amount": amount,
        "category": category,
    }

    expenses.append(expense)


expenses = load_expenses()

add_expense(
    expenses,
    "Lunch",
    150,
    "Food",
)

save_expenses(expenses)

print("Python Practice Day 9")
print("Expense saved successfully.")