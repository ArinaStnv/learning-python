import random
min_num, max_num= map(int, input(f'Введите два числа через пробел:').split())
guess = random.randint(min_num, max_num)
number = None
counter = 0
while number != guess:
    counter += 1
    number = input(f'Введите число: ')
    if not number.isdigit():
        print('Вы ввели не число, введите число:')
        continue
    number = int(number)
    if number < guess:
        print(f'Число больше загаданного')
    elif number > guess:
        print(f'Число меньше загаданного')
    else:
        print(f'Вы угадали число {guess} за {counter} попыток')


 