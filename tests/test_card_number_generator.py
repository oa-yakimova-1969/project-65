import pytest

from src.generators import card_number_generator


@pytest.mark.parametrize(
    "start, stop, expected_result",
    [
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
        (99999, 100000, ["0000 0000 0009 9999", "0000 0000 0010 0000"]),
        (5, 1, ["Ошибка ввода"]),
        (5, 5, ["Ошибка ввода"]),
        (9999999999999999, 10000000000000005, ["9999 9999 9999 9999"]),
    ],
)
def test_card_number_generator(start, stop, expected_result):
    generator = list(card_number_generator(start, stop))
    assert generator == expected_result
