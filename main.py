from src.widget import get_date, mask_account_card

info = input("Введите номер карты или счета:")
date_str = input("Введите дату:")

print(mask_account_card(info))
print(get_date(date_str))
