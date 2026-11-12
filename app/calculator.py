"""Простой калькулятор — демо-приложение для лекции по CI/CD."""


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        raise ValueError("Деление на ноль!")
    return a / b
