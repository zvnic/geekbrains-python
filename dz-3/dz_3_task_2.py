"""
2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
"""

import random

def getListRandomValue(size):
    return random.sample(range(1, size + 1), size)

def multiplicationPairsNumbers(arr):
    result = []
    for i in range(len(arr)):
        if i <= (len(arr)-1) - i:
            result.append(arr[i] * arr[(len(arr)-1) - i])
    return result

arr = getListRandomValue(5)
print(f"Список: {arr}")
print(f"Произведение пар чисел списка: {multiplicationPairsNumbers(arr)}")
