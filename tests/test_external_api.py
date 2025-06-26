from unittest.mock import patch

from src.external_api import get_transaction_amount

transaction_ = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {"amount": "100.00", "currency": {"name": "USD", "code": "USD"}},
}


@patch("requests.get")
def test_get_transaction_amount_success(mock_get):
    """Тест на успешный запрос когда сумма в валюте"""
    expected = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 100},
        "info": {"timestamp": 1744464485, "rate": 83.179878},
        "date": "2025-04-12",
        "result": 8317.9878,
    }
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = expected
    assert get_transaction_amount(transaction_) == expected["result"]


@patch("requests.get")
def test_get_transaction_amount_unsuccess(mock_get):
    """Тест на неуспешный запрос когда сумма в валюте"""
    mock_get.return_value.status_code = 401
    mock_get.return_value.json.return_value = None
    assert get_transaction_amount(transaction_) is None


transaction_rub = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {"amount": "300.00", "currency": {"name": "руб.", "code": "RUB"}},
}


def test_get_transaction_amount_rub():
    """Тест когда сумма в рублях"""
    assert get_transaction_amount(transaction_rub) == 300.00
