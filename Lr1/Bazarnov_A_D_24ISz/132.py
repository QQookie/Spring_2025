def is_brackets_balanced(s: str) -> bool:
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets:
            if not stack or stack.pop() != brackets[char]:
                return False

    return not stack

# Тесты
test_cases = [
    ("(a + b) * {c / [d - e]}", True),
    ("(a + b))", False),
    ("{[()()]}", True),
    ("(]", False),
    ("((()))", True),
    ("{[}", False)
]

for expr, expected in test_cases:
    print(f"Строка: {expr} -> Баланс: {is_brackets_balanced(expr)} (Ожидалось: {expected})")