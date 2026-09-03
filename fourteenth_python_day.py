"""My fourteenth day practicing Python."""


class BankAccount:
    """Represent a simple bank account."""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Add money to the account."""

        self.balance += amount

        return self.balance

    def display_balance(self):
        """Display the current balance."""

        return (
            f"{self.owner}'s balance: "
            f"{self.balance:.2f} BDT"
        )


account = BankAccount("Ahmed", 1000)

account.deposit(500)

print("Python Practice Day 14")
print(account.display_balance())