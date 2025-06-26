def filter_by_currency(trans, currency):
    """Функция фильтра транзакций по заданной валюте"""
    for tran in trans:
        if tran["operationAmount"]["currency"]["code"] == currency:
            yield tran


def transaction_descriptions(trans):
    """Функция вывода сообщений описания транзакций"""
    for tran in trans:
        yield tran["description"]


def card_number_generator(start, stop):
    """Функция генерирования номера карты в формате ХХХХ ХХХХ ХХХХ ХХХХ"""
    if start < stop:
        for i in range(start, stop + 1):
            if len(str(i)) <= 16:
                count_0 = "0" * (16 - len(str(i)))
                number = count_0 + str(i)
                card_number = f"{number[:4]} {number[4:8]} {number[8:12]} {number[12:]}"
                yield card_number
    else:
        yield "Ошибка ввода"
        