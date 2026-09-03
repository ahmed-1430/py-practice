"""Tests for Day 14."""

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
            self.account.balance,
            1000,
        )

    def test_deposit(self):
        """Test depositing money."""

        self.account.deposit(500)

        self.assertEqual(
            self.account.balance,
            1500,
        )

    def test_withdraw(self):
        """Test withdrawing money."""

        self.account.withdraw(300)

        self.assertEqual(
            self.account.balance,
            700,
        )

    def test_invalid_deposit(self):
        """Test invalid deposit."""

        with self.assertRaises(ValueError):
            self.account.deposit(0)

    def test_invalid_withdraw(self):
        """Test invalid withdrawal."""

        with self.assertRaises(ValueError):
            self.account.withdraw(-100)

    def test_insufficient_balance(self):
        """Test insufficient balance."""

        with self.assertRaises(ValueError):
            self.account.withdraw(2000)


if __name__ == "__main__":
    unittest.main()