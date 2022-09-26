"""
3. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
*Пример:*

- Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
"""

def sequenceСalculation(n):
    res = {i:round((1 + 1 / i)**i, 2) for i in range(1, n+1)}
    return res

n = int(input("Введите число N: "))

print(sequenceСalculation(n))
