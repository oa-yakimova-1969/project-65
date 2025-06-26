from typing import Union

STANDART_LENGTH_CARD_NUMBER = 16
STANDART_LENGTH_ACCOUNT_NUMBER = 20


def get_mask_card_number(card_number: Union[str, int]) -> str:
    """Принимает на вход номер карты и возвращает ее маску"""
    str_card_number = str(card_number)
    if str_card_number.isdigit() and len(str_card_number) == STANDART_LENGTH_CARD_NUMBER:
        return f"{str_card_number[:4]} {str_card_number[4:6]}** **** {str_card_number[12:]}"
    else:
        return "Некорректный ввод"


def get_mask_account(account_number: Union[str, int]) -> str:
    """Принимает на вход номер счета и возвращает его маску"""
    str_account_number = str(account_number)
    if str_account_number.isdigit() and len(str_account_number) == STANDART_LENGTH_ACCOUNT_NUMBER:
        return f"**{str_account_number[-4:]}"
    else:
        return "Некорректный ввод"
