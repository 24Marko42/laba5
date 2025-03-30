# Напишите функцию arithmetic_operation(operation), 
# которая принимает символ одной из четырех арифметических операций, 
# а возвращает функцию двух аргументов для соответствующей операции.

def arithmetic_operation(operation):
    if operation == '+':
        return lambda a, b: a + b
    elif operation == '-':
        return lambda a, b: a - b
    elif operation == '*':
        return lambda a, b: a * b
    elif operation == '/':
        return lambda a, b: a / b if b != 0 else None  # Обработка деления на ноль
    else:
        raise ValueError("Недопустимая операция")

plus = arithmetic_operation('+')
minus = arithmetic_operation('-')
umnozhenie = arithmetic_operation('*')
delenie = arithmetic_operation('/')
print(plus(5, 3))  

print(minus(10, 4))  

print(umnozhenie(6, 7))  

print(delenie(8, 2))  
print(delenie(5, 0))  