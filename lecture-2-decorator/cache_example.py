"""
Пример реализации простого кэша через декоратор
"""
import time


def cache(func):
    # храним значения функции func
    # в зависимости от параметров
    data: dict = {}

    def wrapper(*args, **kwargs):
        # из параметров функции формируем ключ
        key = args + tuple(kwargs.items())

        # если для таких параметров еще не вычислялась функция
        # то вычисляем ее с этими параметрами и сохраняем
        if key not in data:
            data[key] = func(*args, **kwargs)
        
        # возвращаем значение из хранилища
        return data[key]
        
    return wrapper


# Пример чисел Фибоначчи
# 1 1 2 3 5 8 ...
# f(n) = f(n - 1) + f(n - 2),
# где f(n) - n-ое число Фибоначчи
def fib_number(n: int) -> int:
    """
    Вычисляет n-ое число Фибоначчи
    для n = 0, 1 число Фибоначчи равно 1
    для n = 2, число Фибоначчи равно 2
    """
    if n < 0:
        return 0
    elif n in (0, 1):
        return 1

    return fib_number(n - 1) + fib_number(n - 2)

@cache
def fib_number_cached(n: int) -> int:
    """
    Вычисляет n-ое число Фибоначчи
    для n = 0, 1 число Фибоначчи равно 1
    для n = 2, число Фибоначчи равно 2
    """
    if n < 0:
        return 0
    elif n in (0, 1):
        return 1

    return fib_number_cached(n - 1) + fib_number_cached(n - 2)


start_time = time.time()
fib_number(35)
end_time = time.time()
print("Без кэша:",end_time - start_time)

start_time = time.time()
fib_number_cached(35)
end_time = time.time()
print("C кэшом:",end_time - start_time)

#blyat' zaebala eta ebatoria