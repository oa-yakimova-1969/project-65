from unittest.mock import mock_open, patch

from src.utils import get_json_transactions


@patch("builtins.open", new_callable=mock_open, read_data='[{"amount": 100, "currency": "USD"}]')
def test_valid_file(mock_file):
    """Тест на корректный файл с транзакциями"""

    data_transactions = get_json_transactions("data/operations.json")

    assert data_transactions == [{"amount": 100, "currency": "USD"}]


@patch("builtins.open", new_callable=mock_open, read_data="")
def test_empty_file(mock_file):
    """Тест на пустой файл"""

    data_transactions = get_json_transactions("data/operations.json")

    assert data_transactions == []


@patch("builtins.open", new_callable=mock_open, read_data='{"amount": 100}')
def test_not_a_list(mock_file):
    """Тест на некорректные данные (например, не список)"""

    data_transactions = get_json_transactions("data/operations.json")

    assert data_transactions == []


@patch("builtins.open", side_effect=FileNotFoundError)
def test_file_not_found(mock_file):
    """Тест на случай, если файл не найден"""

    data_transactions = get_json_transactions("data/operations.json")

    assert data_transactions == []
