"""My fourteenth day practicing Python."""

from datetime import datetime


class BankAccount:
    """Represent a bank account."""

    def __init__(self, owner, balance=0):
        """Initialize a bank account."""

        if not owner.strip():
            raise ValueError(
                "Account owner cannot be empty."
            )

        if balance < 0:
            raise ValueError(
                "Initial balance cannot be negative."
            )

        self.owner = owner.strip()
        self.balance = balance
        self.transactions = []

    def add_transaction(
        self,
        transaction_type,
        amount,
    ):
        """Add a transaction to history."""

        transaction = {
            "type": transaction_type,
            "amount": amount,
            "balance": self.balance,
            "date": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
        }

        self.transactions.append(
            transaction
        )

    def deposit(self, amount):
        """Deposit money into the account."""

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

        self.add_transaction(
            "Withdrawal",
            amount,
        )

        return self.balance

    def get_transaction_history(self):
        """Return all transactions."""

        return self.transactions.copy()

    def display_balance(self):
        """Return formatted account balance."""

        return (
            f"{self.owner}'s balance: "
            f"{self.balance:.2f} BDT"
        )