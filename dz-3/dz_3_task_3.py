"""
3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
"""

import numpy as np

def getListRandomValue(size):
    return np.random.random_sample(size).round(2)

def differenceBetweenMaxMinValue(arr):
    minValue = arr[0] % 1
    maxValue = arr[0] % 1

    for i in range(len(arr)):
        if arr[i] % 1 > maxValue:
            maxValue = round(arr[i] % 1, 3)
        if arr[i] % 1 > 0 and arr[i] % 1 < minValue:
            minValue = round(arr[i] % 1, 3)

    print(f"{maxValue} - {minValue} = {round((maxValue - minValue), 3)}")

arr = getListRandomValue(5)
print(arr)
differenceBetweenMaxMinValue(arr)