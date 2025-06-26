from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info: str) -> str:
    """Принимает на вход строку, содержащую тип и номер карты или счета,
    и возвращает строку с замаскированным номером"""
    parts = info.split()
    if len(parts) < 2:
        return "Ошибка: некорректный ввод."
    else:
        identifier = " ".join(parts[:-1])
        number = parts[-1]
        if identifier.lower().startswith("счет"):
            masked_info = get_mask_account(number)
            return f"{identifier} {masked_info}"
        else:
            masked_info = get_mask_card_number(number)
            return f"{identifier} {masked_info}"


def get_date(date_str: str) -> str:
    """Функция преобразования формата даты"""
    date_part = date_str.split("T")[0]  # Берем только дату
    if date_part:
        parts = date_part.split("-")
        new_parts = parts[::-1]
        new_date = ".".join(new_parts)
        return new_date
    else:
        return "Введены некорректные данные"
