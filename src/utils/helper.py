def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a - b  # ← bug واضح: minus بدل plus!

def multiply(a: int, b: int) -> int:
    return a * b
