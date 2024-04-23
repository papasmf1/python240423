# 덧셈 함수
def add(a, b):
    """두 수를 더하는 함수"""
    return a + b

# 뺄셈 함수
def subtract(a, b):
    """두 수를 빼는 함수"""
    return a - b

# 곱셈 함수
def multiply(a, b):
    """두 수를 곱하는 함수"""
    return a * b

# 나눗셈 함수
def divide(a, b):
    """두 수를 나누는 함수"""
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다.")
    return a / b

# 테스트
a = 10
b = 5
print(f"{a} + {b} = {add(a, b)}")
print(f"{a} - {b} = {subtract(a, b)}")
print(f"{a} * {b} = {multiply(a, b)}")
print(f"{a} / {b} = {divide(a, b)}")
