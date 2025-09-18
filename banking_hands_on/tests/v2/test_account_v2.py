from unittest.mock import MagicMock

import pytest

from banking_hands_on.src.v2.account import Account


# @pytest.fixture()
# def mock_db() -> Account:
#     return Account(account_number="123456", initial_balance=100.0)

@pytest.fixture(scope="function")
def account() -> Account:
    db_connection = MagicMock()
    db_connection.save_account.return_value = True
    return Account(account_number="123456", db_connection=db_connection, initial_balance=100.0)


def test_deposit(account: Account) -> None:
    account.deposit(50.0)
    assert account.get_balance() == 150.0


def test_initial_balance(account: Account) -> None:
    assert account.get_balance() == 100.0


def test_withdraw(account: Account) -> None:
    account.withdraw(30.0)
    assert account.get_balance() == 70.0


def test_withdraw_insufficient_funds(account: Account) -> None:
    with pytest.raises(ValueError, match="Insufficient funds."):
        account.withdraw(200.0)


def test_deposit_negative_amount(account: Account) -> None:
    with pytest.raises(ValueError, match="Deposit amount must be positive."):
        account.deposit(-20.0)


def test_withdraw_negative_amount(account: Account) -> None:
    with pytest.raises(ValueError, match="Withdrawal amount must be positive."):
        account.withdraw(-10.0)
