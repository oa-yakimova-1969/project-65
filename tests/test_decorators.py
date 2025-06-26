import os

import pytest

from src.decorators import log


@log(filename="mylog.txt")
def add(x, y):
    return x + y


def test_log_add_success():
    """Тестирует успешное выполнение декорированной функции"""
    assert add(1, 2) == 3


def test_log_add_error():
    """Тестирует выполнение декорированной функции при возникновении ошибки"""
    with pytest.raises(TypeError):
        add(1, "2")


@log(filename="test_log.txt")
def my_function(x, y):
    return x / y


def test_logging_to_file_success():
    """Тестирует запись в файл после успешного выполнения"""
    if os.path.exists("test_log.txt"):
        os.remove("test_log.txt")

    try:
        my_function(4, 2)
    except ZeroDivisionError:
        pass

    with open("test_log.txt", "r") as file:
        logs = file.readlines()
        assert "my_function ok" in logs[-2]

    os.remove("test_log.txt")


def test_logging_to_file_error():
    """Тестирует запись в файл после ошибки"""
    if os.path.exists("test_log.txt"):
        os.remove("test_log.txt")

    try:
        my_function(4, 0)
    except ZeroDivisionError:
        pass

    with open("test_log.txt", "r") as file:
        logs = file.readlines()
        assert "my_function error" in logs[-2]

    os.remove("test_log.txt")


@log()
def add_function(x, y):
    return x + y


def test_add_function_success(capsys):
    """Тестирует вывод в консоль после успешного выполнения"""
    add_function(1, 2)
    captured = capsys.readouterr()
    assert "add_function ok" in captured.out


def test_faulty_function_error(capsys):
    """Тестирует вывод в консоль после ошибки"""

    @log()
    def faulty_function(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        faulty_function(1, 0)
    captured = capsys.readouterr()
    assert "faulty_function error" in captured.out
