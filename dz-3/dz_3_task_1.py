"""
1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
"""

import random

def getListRandomValue(size):
    arr = random.sample(range(1, size+1), size)
    return arr

def sumOddElements(arr):
    sum = 0
    for i in range(len(arr)):
        if(i % 2 != 0):
            print(f"arr[{i}]={arr[i]}")
            sum += arr[i]
    return sum

arr = getListRandomValue(5)
print(arr)

print(f"Сумма нечётных элементов = {sumOddElements(arr)}")