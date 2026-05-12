"""Shared utility helpers."""


def greet(name: str) -> str:
    return f"Hello, {name}!"


def add(a: int, b: int) -> int:
    return a + b


def process_data(data: list) -> list:
    return [x * 2 for x in data if isinstance(x, (int, float))]
