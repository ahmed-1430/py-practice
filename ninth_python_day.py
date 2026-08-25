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


print("Python Practice Day 9")

for expense in expenses:
    print(
        f"{expense['title']} - "
        f"{expense['amount']} BDT - "
        f"{expense['category']}"
    )