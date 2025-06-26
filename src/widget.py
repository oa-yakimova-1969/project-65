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