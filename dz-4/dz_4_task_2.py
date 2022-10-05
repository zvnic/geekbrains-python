"""
Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
"""

def getNaturalNumbers(n):
    listNumbers = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            listNumbers.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        listNumbers.append(n)
    return listNumbers

num = int(input("Введите число N: "))

print(f"Список множителей числа {num}: {getNaturalNumbers(num)}")
