"""
Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
Пример:
- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
"""

from random import randint
import itertools


def getRatios(k):
    ratios = [randint(0, 10) for i in range(k + 1)]
    while ratios[0] == 0:
        ratios[0] = randint(1, 10)
    return ratios


def getPolynomial(k, ratios):
    template = ['*x^'] * (k - 1) + ['*x']
    polynomial = [[a, b, c] for a, b, c in itertools.zip_longest(ratios, template, range(k, 1, -1), fillvalue='') if a != 0]
    for x in polynomial:
        x.append(' + ')
    polynomial = list(itertools.chain(*polynomial))
    polynomial[-1] = ' = 0'
    return "".join(map(str, polynomial)).replace(' 1*x', ' x')


k = randint(2, 7)
polynom_1 = getPolynomial(k, getRatios(k))
print(f'Многочлен степени {k} = {polynom_1}')

k = randint(2, 7)
polynom_2 = getPolynomial(k, getRatios(k))
print(f'Многочлен степени {k} = {polynom_2}')

# сохраняем ответы в файлы для следующей задачи
with open('dz_4_task_4_polynom_1.txt', 'w') as data:
    data.write(polynom_1)

with open('dz_4_task_4_polynom_2.txt', 'w') as data:
    data.write(polynom_2)
