from typing import Any


def filter_by_state(transactions: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """Функция фильтрации операций по ключу 'state'"""
    filtered_transactions = []
    for transaction in transactions:
        if transaction["state"] == state:
            filtered_transactions.append(transaction)
    return filtered_transactions


def sort_by_date(transactions: list[dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:
    """Функция сортировки операций по дате"""
    sorted_transactions = sorted(transactions, key=lambda transaction: transaction["date"], reverse=reverse)
    return sorted_transactions
