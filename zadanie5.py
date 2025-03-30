# Напишите декоратор check_password, который запрашивает пароль, прежде чем вызвать функцию,
# если он неверный - возвращает None и печатает «В доступе отказано».

def check_password(func):
    def wrapper(*args, **kwargs):
        password = input("Введите пароль: ")  # Запрашиваем пароль у пользователя
        if password == "secret":  # Проверяем, совпадает ли он с заданным
            return func(*args, **kwargs)  # Если да, вызываем оригинальную функцию
        else:
            print("В доступе отказано")  # Если нет, выводим сообщение
            return None  # Возвращаем None
    return wrapper

@check_password  # Применяем декоратор к функции
def secret_function():
    print("SECRET INFOMATION")

# Вызовем функцию для проверки работы декоратора
secret_function()