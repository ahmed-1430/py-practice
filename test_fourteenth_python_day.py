"""Tests for Day 14."""

import unittest

from fourteenth_python_day import BankAccount


class TestBankAccount(unittest.TestCase):
    """Test the BankAccount class."""

    def test_account_creation(self):
        """Test account creation."""

        account = BankAccount(
            "Ahmed",
            1000,
        )

        self.assertEqual(
            account.owner,
            "Ahmed",
        )

        self.assertEqual(
            account.balance,
            1000,
        )


if __name__ == "__main__":
    unittest.main()