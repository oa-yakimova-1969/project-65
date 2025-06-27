from src.decorators import log
from src.external_api import get_transaction_amount
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.readers import read_csv_transactions, read_excel_transactions
from src.services import number_of_transactions, search_for_trans
from src.utils import get_json_transactions
from src.widget import get_date, mask_account_card

card_number = input("Введите номер карты:")
account_number = input("Введите номер счета:")

print(get_mask_card_number(card_number))
print(get_mask_account(account_number))

info = input("Введите номер карты или счета:")
date_str = input("Введите дату:")

transactions = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

# так как список transactions уже есть, назовем список trans
trans = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]

category_list = [
    "перевод организации",
    "перевод со счета на счет",
    "перевод с карты на карту",
]


print(mask_account_card(info))
print(get_date(date_str))
print(filter_by_state(transactions, state="EXECUTED"))
print(sort_by_date(transactions, reverse=True))

usd_transactions = filter_by_currency(trans, "USD")
for _ in range(2):
    print(next(usd_transactions))


descriptions = transaction_descriptions(trans)
for _ in range(5):
    print(next(descriptions))

for card_number in card_number_generator(1, 5):
    print(card_number)


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


my_function(1, 2)

data_transactions = get_json_transactions("data/operations.json")
print(data_transactions)

transaction_ = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {"amount": "100.00", "currency": {"name": "USD", "code": "USD"}},
}

transaction_amount = get_transaction_amount(transaction_)
print(transaction_amount)

print(read_csv_transactions("data/transactions.csv"))

print(read_excel_transactions("data/transactions_excel.xlsx"))

print(search_for_trans(trans, "перевод организации"))

print(number_of_transactions(trans, category_list))


def main():
    """Функция, которая выдает список транзакций по выбранному файлу."""
    print(
        """Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла"""
    )
    file_type = input("Пользователь: ")
    if file_type == "1":
        print("Программа: Для обработки выбран JSON-файл.")
        load_transactions = get_json_transactions("data/operations.json")
    elif file_type == "2":
        print("Программа: Для обработки выбран CSV-файл.")
        load_transactions = read_csv_transactions("data/transactions.csv")
    elif file_type == "3":
        print("Программа: Для обработки выбран XLSX-файл.")
        load_transactions = read_excel_transactions("data/transactions_excel.xlsx")
    state_list = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        status = input(
            """Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"""
        ).upper()
        if status not in state_list:
            print(f'Статус операции "{status}" недоступен.')
        else:
            break
    filtered_transactions = filter_by_state(load_transactions, status)
    print(f'Операции отфильтрованы по статусу "{status}"')
    sort = input("Отсортировать операции по дате? Да/Нет.\n").lower()
    if sort == "да":
        sort_way = input("Отсортировать по возрастанию или по убыванию?\n").lower()
        if sort_way == "по возрастанию":
            date_flag = False
        elif sort_way == "по убыванию":
            date_flag = True
        sorted_transactions = sort_by_date(filtered_transactions, date_flag)
    elif sort == "нет":
        sorted_transactions = filtered_transactions
    print_rub = input("Выводить только рублевые транзакции? Да/Нет\n").lower()
    if print_rub == "да":
        if file_type == "1":
            rub_sort = filter_by_currency(sorted_transactions, "RUB")
            rub_transactions = list(rub_sort)
        elif file_type == "2" or file_type == "3":
            rub_transactions = []
            for tran in sorted_transactions:
                if tran["currency_code"] == "RUB":
                    rub_transactions.append(tran)
    elif print_rub == "нет":
        rub_transactions = sorted_transactions
    filter_by_word = input(
        """Отфильтровать список транзакций по определенному слову
в описании? Да/Нет\n"""
    ).lower()
    if filter_by_word == "да":
        word = input("Введите слово:\n").capitalize()
        search_transactions = search_for_trans(rub_transactions, word)
    elif filter_by_word == "нет":
        search_transactions = rub_transactions
    print("Распечатываю итоговый список транзакций...")
    if len(search_transactions) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(search_transactions)}\n")
    if file_type == "1":
        for i in search_transactions:
            currency = i.get("operationAmount", {}).get("currency", {}).get("name")
            i_data = get_date(i.get("date", ""))
            amount = i.get("operationAmount", {}).get("amount")
            if i.get("description") == "Открытие вклада":
                from_to = mask_account_card(i.get("to", ""))
            else:
                from_to = mask_account_card(i.get("from", "")) + " -> " + mask_account_card(i.get("to", ""))
            print(f"{i_data} {i.get("description", "")}\n{from_to}\nСумма: {amount} {currency}\n")
    elif file_type == "2" or file_type == "3":
        for i in search_transactions:
            currency = i.get("currency_code", "")
            i_data = get_date(i.get("date", ""))
            amount = i.get("amount", "")
            if i.get("description") == "Открытие вклада":
                from_to = mask_account_card(i.get("to", ""))
            else:
                from_to = mask_account_card(i.get("from", "")) + " -> " + mask_account_card(i.get("to", ""))
            print(f"{i_data} {i.get("description", "")}\n{from_to}\nСумма: {amount} {currency}\n")


main()
