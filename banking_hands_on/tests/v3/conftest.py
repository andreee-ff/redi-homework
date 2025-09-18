import pytest
from unittest.mock import MagicMock


@pytest.fixture()
def db_connection_mock():
    db_connection_mock = MagicMock()
    db_connection_mock.save_account.return_value = True
    return db_connection_mock
