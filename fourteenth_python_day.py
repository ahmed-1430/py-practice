"""My fourteenth day practicing Python."""

from datetime import datetime


class BankAccount:
    """Represent a simple bank account."""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transactions = []

    def add_transaction(self, transaction_type, amount):
        """Save a transaction."""

        transaction = {
            "type": transaction_type,
            "amount": amount,
            "date": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
        }

        self.transactions.append(
            transaction
        )

    def deposit(self, amount):
        """Add valid money to the account."""

        if amount <= 0:
            raise ValueError(
                "Deposit amount must be greater than zero."
            )

        self.balance += amount

        self.add_transaction(
            "Deposit",
            amount,
        )

        return self.balance

    def withdraw(self, amount):
        """Withdraw valid money."""

        if amount <= 0:
            raise ValueError(
                "Withdrawal amount must be greater than zero."
            )

        if amount > self.balance:
            raise ValueError(
                "Insufficient balance."
            )

        self.balance -= amount

        self.add_transaction(
            "Withdrawal",
            amount,
        )

        return self.balance

    def get_transaction_history(self):
        """Return transaction history."""

        return self.transactions

    def display_balance(self):
        """Display current balance."""

        return (
            f"{self.owner}'s balance: "
            f"{self.balance:.2f} BDT"
        )


if __name__ == "__main__":
    account = BankAccount("Ahmed", 1000)

    account.deposit(500)
    account.withdraw(200)

    print("Python Practice Day 14")
    print(account.display_balance())

    print("\nTransactions:")

    for transaction in (
        account.get_transaction_history()
    ):
        print(
            f"{transaction['type']} - "
            f"{transaction['amount']} BDT"
        )