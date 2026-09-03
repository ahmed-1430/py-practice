"""Tests for Day 14."""

import unittest

from fourteenth_python_day import BankAccount


class TestBankAccount(unittest.TestCase):
    """Test the BankAccount class."""

    def setUp(self):
        """Create a fresh account before each test."""

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


if __name__ == "__main__":
    unittest.main()