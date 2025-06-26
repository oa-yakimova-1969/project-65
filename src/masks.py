import logging
from typing import Union

STANDART_LENGTH_CARD_NUMBER = 16
STANDART_LENGTH_ACCOUNT_NUMBER = 20

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/masks.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: Union[str, int]) -> str:
    """Принимает на вход номер карты и возвращает ее маску"""
    logger.debug("Функция маскировки номера карты начала работу")
    logger.debug("Преобразуем входные данные в строку")
    str_card_number = str(card_number)
    logger.debug("Проверяем входные данные на корректность")
    if str_card_number.isdigit() and len(str_card_number) == STANDART_LENGTH_CARD_NUMBER:
        logger.debug("Функция маскировки номера карты успешно завершилась\n")
        return f"{str_card_number[:4]} {str_card_number[4:6]}** **** {str_card_number[12:]}"
    else:
        logger.error("Функция маскировки номера карты завершилась с ошибкой\n")
        return "Некорректный ввод"


def get_mask_account(account_number: Union[str, int]) -> str:
    """Принимает на вход номер счета и возвращает его маску"""
    logger.debug("Функция маскировки номера счета начала работу")
    logger.debug("Преобразуем входные данные в строку")
    str_account_number = str(account_number)
    logger.debug("Проверяем входные данные на корректность")
    if str_account_number.isdigit() and len(str_account_number) == STANDART_LENGTH_ACCOUNT_NUMBER:
        logger.debug("Функция маскировки номера счета успешно завершилась\n")
        return f"**{str_account_number[-4:]}"
    else:
        logger.error("Функция маскировки номера счета завершилась с ошибкой\n")
        return "Некорректный ввод"
