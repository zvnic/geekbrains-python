"""
2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
*Пример:*

- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
"""


def getMultiplicationOfNumbers(n):
    res = [factorial(i) for i in range(1, n+1)]
    return res

def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact

n = int(input("Введите число N: "))

print(getMultiplicationOfNumbers(n))
