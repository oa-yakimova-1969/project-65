from typing import Union

import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "input_card_number, expected_card_number",
    [(9999888877776666, "9999 88** **** 6666"), ("9999888877776666", "9999 88** **** 6666")],
)
def test_get_mask_card_number(input_card_number: Union[str, int], expected_card_number: str) -> None:
    assert get_mask_card_number(input_card_number) == expected_card_number


def test_get_mask_card_number_incorrect_length() -> None:
    assert get_mask_card_number(99998888777766665555) == "Некорректный ввод"
    assert get_mask_card_number("99998888") == "Некорректный ввод"


def test_get_mask_card_number_incorrect_format() -> None:
    assert get_mask_card_number("Abcd@#$%;:[}") == "Некорректный ввод"


def test_get_mask_card_number_empty() -> None:
    assert get_mask_card_number("") == "Некорректный ввод"


@pytest.mark.parametrize(
    "input_account, expected_account", [(99998888777766665555, "**5555"), ("99998888777766665555", "**5555")]
)
def test_get_mask_account(input_account: Union[str, int], expected_account: str) -> None:
    assert get_mask_account(input_account) == expected_account


def test_get_mask_account_incorrect_length() -> None:
    assert get_mask_account(888877776666555544443333) == "Некорректный ввод"
    assert get_mask_account("88887777") == "Некорректный ввод"


def test_get_mask_account_incorrect_format() -> None:
    assert get_mask_account("Abcd@#$%;:[}<>?!") == "Некорректный ввод"


def test_get_mask_account_empty() -> None:
    assert get_mask_account("") == "Некорректный ввод"
