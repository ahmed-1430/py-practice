"""Tests for Day 14 BankAccount."""

import unittest

from fourteenth_python_day import BankAccount


class TestBankAccount(unittest.TestCase):
    """Test the BankAccount class."""

    def setUp(self):
        """Create a fresh account."""

        self.account = BankAccount(
            "Ahmed",
            1000,
        )

    def test_account_creation(self):
        """Test account creation."""

        self.assertEqual(
            self.account.owner,
            "Ahmed",
        )

        self.assertEqual(
            self.account.balance,
            1000,
        )

    def test_deposit(self):
        """Test depositing money."""

        result = self.account.deposit(500)

        self.assertEqual(
            result,
            1500,
        )

        self.assertEqual(
            self.account.balance,
            1500,
        )

    def test_withdraw(self):
        """Test withdrawing money."""

        result = self.account.withdraw(300)

        self.assertEqual(
            result,
            700,
        )

        self.assertEqual(
            self.account.balance,
            700,
        )

    def test_invalid_deposit(self):
        """Test invalid deposits."""

        with self.assertRaises(ValueError):
            self.account.deposit(0)

        with self.assertRaises(ValueError):
            self.account.deposit(-100)

    def test_invalid_withdraw(self):
        """Test invalid withdrawals."""

        with self.assertRaises(ValueError):
            self.account.withdraw(0)

    def test_insufficient_balance(self):
        """Test withdrawing too much money."""

        with self.assertRaises(ValueError):
            self.account.withdraw(2000)

    def test_invalid_owner(self):
        """Test empty account owner."""

        with self.assertRaises(ValueError):
            BankAccount("")

    def test_negative_initial_balance(self):
        """Test negative initial balance."""

        with self.assertRaises(ValueError):
            BankAccount("Ahmed", -100)

    def test_transaction_history(self):
        """Test transaction history."""

        self.account.deposit(500)
        self.account.withdraw(200)

        transactions = (
            self.account.get_transaction_history()
        )

        self.assertEqual(
            len(transactions),
            2,
        )

        self.assertEqual(
            transactions[0]["type"],
            "Deposit",
        )

        self.assertEqual(
            transactions[0]["amount"],
            500,
        )

        self.assertEqual(
            transactions[1]["type"],
            "Withdrawal",
        )

        self.assertEqual(
            transactions[1]["amount"],
            200,
        )


if __name__ == "__main__":
    unittest.main()