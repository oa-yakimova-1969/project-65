from src.masks import get_mask_account, get_mask_card_number

card_number = input("Введите номер карты:")
account_number = input("Введите номер счета:")

print(get_mask_card_number(card_number))
print(get_mask_account(account_number))
