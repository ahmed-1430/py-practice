"""My ninth day practicing Python."""


def get_amount():
    """Get a valid amount from the user."""

    while True:
        try:
            amount = float(input("Enter expense amount: "))

            if amount <= 0:
                print("Amount must be greater than zero.")
                continue

            return amount

        except ValueError:
            print("Please enter a valid number.")


print("Python Practice Day 9")

amount = get_amount()

print(f"You entered: {amount:.2f} BDT")