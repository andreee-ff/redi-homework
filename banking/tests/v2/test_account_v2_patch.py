import pytest
from unittest.mock import patch, MagicMock

from banking.src.v2.account import Account

@pytest.fixture(autouse=True)
def patch_db_connection():
    with patch("banking.src.v2.account.DatabaseConnection") as MockDB:
        mock_db = MagicMock()
        mock_db.save_account.return_value = None
        mock_db.get_account.return_value = 100.0
        MockDB.return_value = mock_db
        yield mock_db

@pytest.fixture
def account():
    # DatabaseConnection is patched automatically
    return Account(account_number="MOCK123", initial_balance=100.0)

def test_deposit_calls_save_account(account, patch_db_connection):
    account.deposit(50.0)
    patch_db_connection.save_account.assert_called_with("MOCK123", 150.0)

def test_withdraw_calls_save_account(account, patch_db_connection):
    account.withdraw(30.0)
    patch_db_connection.save_account.assert_called_with("MOCK123", 70.0)

def test_get_balance_calls_save_account(account, patch_db_connection):
    account.get_balance()
    patch_db_connection.save_account.assert_called_with("MOCK123")
