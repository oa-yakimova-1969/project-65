import csv

import pandas as pd


def read_csv_transactions(csv_path):
    """Функция чтения csv файла"""
    try:
        with open(csv_path, "r", encoding="UTF-8") as f:
            csv_reader = csv.DictReader(f, delimiter=";")
            csv_transactions = list(csv_reader)
            return csv_transactions
    except Exception:
        return []


def read_excel_transactions(excel_path):
    """Функция чтения excel файла"""
    try:
        excel_reader = pd.read_excel(excel_path)
        excel_transactions = excel_reader.to_dict(orient="records")
        return excel_transactions
    except Exception:
        return []
