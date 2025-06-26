from unittest.mock import mock_open, patch

import pandas as pd

from src.readers import read_csv_transactions, read_excel_transactions


@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data=("id;state;date;amount;currency_name;currency_code;from;to;description\n1;2;3;4;5;6;7;8;9\n"),
)
def test_read_csv_transactions_correct(mock_file):
    """Тест на корректный csv файл с транзакциями"""
    result = read_csv_transactions("fake")
    assert result == [
        {
            "id": "1",
            "state": "2",
            "date": "3",
            "amount": "4",
            "currency_name": "5",
            "currency_code": "6",
            "from": "7",
            "to": "8",
            "description": "9",
        }
    ]


@patch("builtins.open", new_callable=mock_open, read_data="")
def test_read_empty_csv(mock_file):
    """Тест на пустой файл"""
    result = read_csv_transactions("fake")
    assert result == []


@patch("builtins.open", new_callable=mock_open, read_data=("a1@"))
def test_read_uncorrect_data(mock_file):
    """Тест на некорректные данные"""
    result = read_csv_transactions("fake")
    assert result == []


@patch("builtins.open", side_effect=FileNotFoundError)
def test_file_not_found(mock_file):
    """Тест на случай, если файл не найден"""
    result = read_csv_transactions("fake")
    assert result == []


@patch("pandas.read_excel")
def test_read_excel_transactions_correct(mock_read_excel):
    """Тест на корректный excel файл с транзакциями"""
    mock_data = pd.DataFrame({"id": ["1", "2", "3"], "Amount": ["100", "200", "300"]})
    mock_read_excel.return_value = mock_data
    result = read_excel_transactions("fake")
    expected = [
        {"id": "1", "Amount": "100"},
        {"id": "2", "Amount": "200"},
        {"id": "3", "Amount": "300"},
    ]
    assert result == expected


@patch("pandas.read_excel")
def test_read_empty_excel(mock_read_excel):
    """Тест на пустой файл"""
    mock_data = pd.DataFrame({})
    mock_read_excel.return_value = mock_data
    result = read_excel_transactions("fake")
    expected = []
    assert result == expected
