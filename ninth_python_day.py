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
        return []


def save_expenses(expenses):
    """Save expenses to JSON."""

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses, title, amount, category):
    """Add a new expense with the current date."""

    expense = {
        "title": title,
        "amount": amount,
        "category": category,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
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

for expense in expenses:
    print(
        f"{expense['date']} | "
        f"{expense['title']} | "
        f"{expense['amount']} BDT"
    )