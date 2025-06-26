import json
import logging

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/utils.log", mode="w", encoding="UTF-8")
file_formatter = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_json_transactions(file_path):
    """Функция чтения json-файла"""
    logger.debug("Функция чтения json-файла начала работу")
    try:
        logger.debug("Явно указываем режим открытия файла{file_path}")
        with open(file_path, "r", encoding="utf-8") as f:
            logger.debug("Получение данных из файла{file_path}")
            json_transactions = json.load(f)
            logger.debug("Проверяем являются ли данные списком")
            if isinstance(json_transactions, list):
                logger.debug("Функция чтения json-файла успешно завершилась\n")
                return json_transactions

            else:
                logger.error("Некорректные данные:не список\n")
                return []

    except (json.JSONDecodeError, FileNotFoundError, ValueError, TypeError, Exception):
        logger.error("Выполнение функции завершилось с ошибкой\n")
        return []
