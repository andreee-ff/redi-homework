
import pytest
from banking_hands_on.src.v3.user import User


@pytest.fixture(autouse=True)
def user(db_connection_mock):
    return User(2, "Potato", db_connection_mock)


def test_user_v3(user: User):
    info = user.get_user_info()
    assert info == {"user_id": 2, "name": "Potato"}
