# Напишите функцию генератор factorials(n), генерирующую последовательность факториалов
# натуральных чисел.


def factorials(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        yield factorial
