"""
Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
"""

listNumbers = list(map(int, input("Введите числа через пробел: ").split()))

print(f"Исходный список: {listNumbers}")

tempListNumbers = []
[tempListNumbers.append(i) for i in listNumbers if i not in tempListNumbers]

print(f"Список из неповторяющихся элементов: {tempListNumbers}")