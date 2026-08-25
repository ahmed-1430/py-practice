"""My ninth day practicing Python."""


expenses = []


def add_expense(expenses, title, amount, category):
    """Add a new expense."""

    expense = {
        "title": title,
        "amount": amount,
        "category": category,
    }

    expenses.append(expense)


add_expense(expenses, "Lunch", 150, "Food")
add_expense(expenses, "Bus", 50, "Transport")
add_expense(expenses, "Coffee", 120, "Food")


print("Python Practice Day 9")

for expense in expenses:
    print(
        f"{expense['title']} - "
        f"{expense['amount']} BDT - "
        f"{expense['category']}"
    )