"""
4. Задайте список из 2N+1 элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
Позиции вводятся с клавиатуры.
"""

from random import randint

def initArray(n):
    initArr = [2 * n]
    for i in range(2*n):
        initArr.append(randint(-n, n))
    return initArr

n = int(input('Введите размер массива: '))
array = initArray(n)
print(f'Вывод массиса: {array}')

index_a = int(input('Введите номер индекса первого элемнта : '))
index_b = int(input('Введиет номер индекса второго элемента: '))

if 0 < index_a > len(array)-1 or 0 < index_b > len(array)-1:
    print('Ошибка номера элемента массива!')
else:
    print(f'Mult of elements: {array[index_a]} * {array[index_b]} =', array[index_a] * array[index_b])
