import time

def calc_time_incorrect(func):
    # текущее время
    start_time = time.time()
    # вызываем функцию func (которая передается в функцию calc_time, как параметр)
    # с параметрами 1 1 и сохраняем результат в переменную res
    res = func(1, 5)
    # получаем текущее время (оно отлично от start_time)
    end_time = time.time()
    # выводим разницу между временем начала и конца
    # то есть получаем время работы функции foo
    print("Calc time:", end_time - start_time)
    # возвращаем res, то есть результат функции func с параметрами 1 1
    return res

def calc_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        return res, end_time - start_time
    
    return wrapper

@calc_time
def sum_numbers(a, b):
    return a + b

def square_number(a):
    return a ** 2

# Что передается в качестве параметра func -> foo
# В 4 строке вызывается func(1, 1) -> foo(1, 1)
# foo(1, 1) возвращает '11'
# calc_time возвращает результат func(1, 1) -> foo(1, 1) -> '11'
# calc_time возвращает 
# print(calc_time_incorrect(sum_numbers))