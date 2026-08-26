"""My ninth day practicing Python."""

import json
from datetime import datetime


DATA_FILE = "expenses.json"


def load_expenses():
    """Load expenses from JSON."""

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
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
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }

    expenses.append(expense)


def calculate_total(expenses):
    """Calculate total expenses."""

    return sum(expense["amount"] for expense in expenses)


def category_summary(expenses):
    """Calculate spending by category."""

    summary = {}

    for expense in expenses:
        category = expense["category"]

        if category not in summary:
            summary[category] = 0

        summary[category] += expense["amount"]

    return summary


expenses = load_expenses()

if not expenses:
    add_expense(expenses, "Lunch", 150, "Food")
    add_expense(expenses, "Bus", 50, "Transport")
    add_expense(expenses, "Coffee", 120, "Food")

    save_expenses(expenses)


print("Python Practice Day 9")

print(f"\nTotal: {calculate_total(expenses):.2f} BDT")

print("\nCategory Summary:")

summary = category_summary(expenses)

for category, amount in summary.items():
    print(f"{category}: {amount:.2f} BDT")