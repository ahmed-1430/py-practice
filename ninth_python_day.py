"""My ninth day practicing Python."""


expenses = [
    {
        "title": "Lunch",
        "amount": 150,
        "category": "Food",
    },
    {
        "title": "Bus",
        "amount": 50,
        "category": "Transport",
    },
]


def calculate_total(expenses):
    """Calculate total expenses."""

    return sum(expense["amount"] for expense in expenses)


print("Python Practice Day 9")

total = calculate_total(expenses)

print(f"Total expenses: {total} BDT")