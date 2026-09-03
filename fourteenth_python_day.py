"""My fourteenth day practicing Python."""


class BankAccount:
    """Represent a simple bank account."""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Add valid money to the account."""

        if amount <= 0:
            raise ValueError(
                "Deposit amount must be greater than zero."
            )

        self.balance += amount

        return self.balance

    def withdraw(self, amount):
        """Withdraw money from the account."""

        if amount <= 0:
            raise ValueError(
                "Withdrawal amount must be greater than zero."
            )

        if amount > self.balance:
            raise ValueError(
                "Insufficient balance."
            )

        self.balance -= amount

        return self.balance

    def display_balance(self):
        """Display the current balance."""

        return (
            f"{self.owner}'s balance: "
            f"{self.balance:.2f} BDT"
        )


print("Python Practice Day 14")
