import pytest
from unittest.mock import patch, MagicMock

from banking_hands_on.src.v2.account import Account


@pytest.fixture
def account():
    # DatabaseConnection is patched automatically
    return Account(account_number="MOCK123", initial_balance=100.0)
