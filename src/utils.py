import json


def get_json_transactions(file_path):
    """Функция чтения json-файла"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            json_transactions = json.load(f)
            if isinstance(json_transactions, list):
                return json_transactions
            else:
                return []

    except (json.JSONDecodeError, FileNotFoundError, ValueError, TypeError, Exception):
        return []
