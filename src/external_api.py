import os

import requests
from dotenv import load_dotenv

transaction_ = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {"amount": "100.00", "currency": {"name": "USD", "code": "USD"}},
}


load_dotenv()
API_KEY = os.getenv("API_KEY")
url = "https://api.apilayer.com/exchangerates_data/convert"


def get_transaction_amount(transaction_):
    """Функция конвертации валюты"""
    amount = 0
    currency_code = transaction_["operationAmount"]["currency"]["code"]
    amount_transaction = transaction_["operationAmount"]["amount"]
    if currency_code != "RUB":
        try:
            payload = {"amount": f"{amount_transaction}", "from": f"{currency_code}", "to": "RUB"}

            headers = {"apikey": f"{API_KEY}"}
            response = requests.get(url, headers=headers, params=payload)
            status_code = response.status_code
            if status_code == 200:
                data_json = response.json()
                amount += data_json["result"]
                return amount
            else:
                print(status_code)
                print("Запрос не был успешным. Возможная причина: {response.reason}")
        except requests.exceptions.RequestException:
            print("Ошибка конвертации")

    else:
        amount += float(transaction_["operationAmount"]["amount"])
        return amount
