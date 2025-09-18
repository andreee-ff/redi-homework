import pytest

from banking_hands_on.src.v1.account import Account


@pytest.fixture
def account() -> Account:
    return Account(account_number="123456", initial_balance=100.0)


def test_initial_balance(account: Account) -> None:
    assert account.get_balance() == 100.0


@pytest.mark.parametrize(
    "amount, error_message",
    [(50.0, 150.0), (100.0, 200.0), (1.0, 101.0)],
)
def test_generic_nithin(account: Account, amount, error_message):
    account.deposit(amount)
    assert account.get_balance() == error_message


@pytest.mark.parametrize(
    "type_of_error, error_message, amount",
    [
        (ValueError, "Insufficient funds.", 200.0),
        (ValueError, "Withdrawal amount must be positive.", -10.0),
        (TypeError, "Withdrawal amount must be a number.", "potato"),

    ]
)
def test_withdraw_exception(account: Account, type_of_error, error_message, amount):
    with pytest.raises(type_of_error, match=error_message):
        account.withdraw(amount)