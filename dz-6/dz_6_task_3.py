"""
Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
"""

def check(a, b):
    if a > b:
        a, b = b, a
    if a ** 2 == b:
        return 'да'
    else:
        return 'нет'

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
result = check(a, b)
print(f'Число {a} является квадратом числа {b} ? - {result}')
