"""
Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
*Пример:*

- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
"""

def inputNumber():
    return int(input("введите число N: "))

def factorial(x):
    f = lambda x: 1 if x == 0 else x * factorial(x - 1)
    return f(x)

def get_list(n):
    listFactorial = list(factorial(i) for i in range(1, n + 1))
    return listFactorial

print(get_list(inputNumber()))
