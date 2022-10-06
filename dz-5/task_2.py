"""
Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.

Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
a) Добавьте игру против бота
b) Подумайте как наделить бота ""интеллектом""
"""

from random import randint

def stepPlayer(name):
    k = int(input(f"{name}, возьмите конфеты от 1 до 28 штук: "))
    while k < 1 or k > 28:
        k = int(input(f"{name}, введите количество от 1 до 28 штук: "))
    return k


def stepResult(name, k, counter, value):
    print(f"{name}, взял {k} шт., теперь у него всего {counter} шт. Осталось на столе {value} конфет.")

player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
value = int(input("Введите начальное количество конфет на столе: "))

counter1 = 0
counter2 = 0

flag = randint(0,2)

if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

while value > 28:
    if flag:
        k = stepPlayer(player1)
        counter1 += k
        value -= k
        flag = False
        stepResult(player1, k, counter1, value)
    else:
        k = stepPlayer(player2)
        counter2 += k
        value -= k
        flag = True
        stepResult(player2, k, counter2, value)

if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")