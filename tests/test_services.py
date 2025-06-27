import pytest

from src.services import search_for_trans, number_of_transactions

list_operations = [
    {"description": "Оплата услуг", "amount": 100},
    {"description": "Перевод на карту", "amount": 200},
    {"description": "Покупка в магазине", "amount": 300},
]
search_string = "Перевод"
result_expected = [{"description": "Перевод на карту", "amount": 200}]
result = search_for_trans(list_operations, search_string)


@pytest.mark.parametrize(
    "operations, string, expected",
    [(list_operations, search_string, result_expected), ([], search_string, [])],
)
def test_search_for_trans(operations, string, expected):
    assert search_for_trans(operations, string) == expected


operations_list = [
    {"description": "Покупка в магазине"},
    {"description": "Перевод на карту"},
    {"description": "Покупка в магазине"},
    {"description": "Оплата услуг"},
]
category_list = ["покупка в магазине", "перевод на карту", "оплата услуг"]

expected_result = {"покупка в магазине": 2, "перевод на карту": 1, "оплата услуг": 1}


@pytest.mark.parametrize(
    "operations, categories, expected",
    [
        (operations_list, category_list, expected_result),
        ([], category_list, {}),
        (operations_list, [], {}),
    ],
)
def test_number_of_transactions(operations, categories, expected):
    assert number_of_transactions(operations, categories) == expected
