# Проект

## Описание:
Проект - это серверная часть виджета банковских операций. Виджет дает возможность отображать банковские операции клиента.

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/username/project-x.git
```
2. Установите зависимости:
```
pip install -r requirements.txt
```
## Использование:

1. Откройте приложение в вашем веб-браузере.
2. Создайте новый проект и начните добавлять задачи.
3. Назначайте сроки выполнения и приоритеты для задач, чтобы эффективно управлять проектами.

## Документация:

Для получения дополнительной информации обратитесь к [документации](docs/README.md).

## Лицензия:

Этот проект лицензирован по [лицензии MIT](LICENSE).

### Тестирование

Для тестирования проекта используется библиотека `pytest`. Чтобы запустить тесты, выполните команду:

```bash
pytest
```

Тесты покрывают следующие модули и функции:
- `masks`: функции `get_mask_card_number` и `get_mask_account`.
- `widget`: функции `mask_account_card` и `get_date`.
- `processing`: функции `filter_by_state` и `sort_by_date`.
- `generators`: функция `filter_by_currency`, функция-генератор `transaction_descriptions`, генератор `card_number_generator`

Покрытие тестами составляет более 80% кода проекта.

## Модуль Generators

Модуль `generators` предоставляет функции для работы с массивами транзакций. Он включает в себя следующие функции:

- `filter_by_currency(transactions, currency)`: фильтрует транзакции по заданной валюте и возвращает итератор.
- `transaction_descriptions(transactions)`: генератор, возвращающий описания транзакций.
- `card_number_generator(start, stop)`: генератор, который выводит номера банковских карт в формате ХХХХ ХХХХ ХХХХ ХХХХ.

### Примеры использования:


#### Пример использования filter_by_currency
usd_transactions = filter_by_currency(transactions, 'USD')
for transaction in usd_transactions:
    print(transaction)

#### Пример использования transaction_descriptions
for description in transaction_descriptions(transactions):
    print(description)

#### Пример использования card_number_generator
for card in card_number_generator(4000123456789010, 4000123456789015):
    print(card)

## Модуль Decorators

Модуль содержит декоратор `log`, который логирует выполнение функций.

#### Пример использования декоратора

@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)

Ожидаемый вывод в лог-файл 
mylog.txt
 при успешном выполнении:

my_function ok

Ожидаемый вывод при ошибке:

my_function error: тип ошибки. Inputs: (1, 2), {}

Где 
тип ошибки
 заменяется на текст ошибки.

### Модуль для работы с CSV и Excel файлами

- `read_csv_transactions(file_path: str) -> List[Dict]`: Считывает финансовые операции из CSV файла и возвращает список словарей с транзакциями.
- `read_excel_transactions(file_path: str) -> List[Dict]`: Считывает финансовые операции из Excel файла и возвращает список словарей с транзакциями.

### Примеры использования

```python
from my_module import read_csv_transactions, read_excel_transactions

# Пример использования функции для CSV
csv_transactions = read_csv_transactions('path/to/transactions.csv')
print(csv_transactions)

# Пример использования функции для Excel
excel_transactions = read_excel_transactions('path/to/transactions.xlsx')
print(excel_transactions)
