"""My ninth day practicing Python."""


expenses = []


def add_expense(expenses, title, amount, category):
    """Add a validated expense."""

    if not title.strip():
        print("Expense title cannot be empty.")
        return False

    if amount <= 0:
        print("Amount must be greater than zero.")
        return False

    if not category.strip():
        print("Category cannot be empty.")
        return False

    expense = {
        "title": title,
        "amount": amount,
        "category": category,
    }

    expenses.append(expense)

    return True


add_expense(expenses, "Lunch", 150, "Food")
add_expense(expenses, "Bus", 50, "Transport")
add_expense(expenses, "", 100, "Food")
add_expense(expenses, "Coffee", -20, "Food")


print("Python Practice Day 9")

for expense in expenses:
    print(expense)