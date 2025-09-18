from decimal import Decimal
from unittest.mock import MagicMock
import pytest
from banking_hands_on.src.v3.account import Account



@pytest.fixture()
def account(db_connection_mock) -> Account:
    user_mock = MagicMock()
    return Account(account_number="123456", user=user_mock, db_connection=db_connection_mock, initial_balance=100.0)


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
def test_floating_number() -> None:
    from pytest import approx
    assert 0.1 + 0.2 == approx(0.3)

def fibonaci(n):
    if n == 0 or n == 1: return 1
    if n == 2: return 2
    return fibonaci(n - 1) + fibonaci(n - 2)

def test_fibonaci():
    magic_mock = MagicMock()
    magic_mock.fibonnaci(5)
    magic_mock.assert_called_once()
    # assert fibonaci(5) == 8

def expect_bool(boolean):

    return 5 + boolean
def test_expect_bool():
    assert expect_bool("True") == 6
    assert expect_bool(False) == 5
    assert expect_bool(0) == 5
    assert expect_bool(1) == 6
    assert expect_bool(2) == 7
