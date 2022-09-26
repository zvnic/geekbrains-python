"""
1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
*Пример:*

- 6782 -> 23
- 0,56 -> 11
"""

def getSumDigital(n):
    sum = 0
    for i in number:
        sum += int(i)
    return sum

number = input("Введите вещественное число: ").replace(".", "").replace(",", "")

print(getSumDigital(number))