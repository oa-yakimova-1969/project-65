def filter_by_state(transactions: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """Функция фильтрации операций по ключу 'state'"""
    filtered_transactions = []
    for transaction in transactions:
        if transaction["state"] == state:
            filtered_transactions.append(transaction)
    return filtered_transactions
