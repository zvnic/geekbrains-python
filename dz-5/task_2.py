"""
Создайте программу для игры в ""Крестики-нолики"".
"""
import os

# карта с индексами
maps = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# победные линийи
winLine = [[0, 1, 2],[3, 4, 5],[6, 7, 8],[0, 3, 6],[1, 4, 7],[2, 5, 8],[0, 4, 8],[2, 4, 6]]

# Вывод карты
def print_maps():
    print(f"{maps[0]} {maps[1]} {maps[2]}")
    print(f"{maps[3]} {maps[4]} {maps[5]}")
    print(f"{maps[6]} {maps[7]} {maps[8]}")

# ход в клетку
def stepPlayer(step, symbol):
    ind = maps.index(step)
    maps[ind] = symbol

# определяем рузультат
def getWinLine():
    win = ""

    for i in winLine:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = "X"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            win = "O"

    return win


game_over = False
player = True

while game_over == False:

    print_maps()

    if player == True:
        symbol = "X"
        step = int(input("Игрок Х, ваш ход, укажите номер клетки: "))
    else:
        symbol = "O"
        step = int(input("Игрок О, ваш ход, укажите номер клетки: "))

    stepPlayer(step, symbol)
    win = getWinLine()

    if win != "":
        game_over = True
    else:
        game_over = False

    player = not player

print_maps()
print("Победил", win)