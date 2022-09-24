# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится)

def checkQuarter(coordPoint):
    quarter = 4
    if coordPoint[0] > 0 and coordPoint[1] > 0:
        quarter = 1
    elif coordPoint[0] < 0 and coordPoint[1] > 0:
        quarter = 2
    elif coordPoint[0] < 0 and coordPoint[1] < 0:
        quarter = 3
    print(f"Точка находится в {quarter} четверти плоскости")

def inputCoordinatePoint():
    xy = ["X", "Y"]
    arr = []
    for i in range(len(xy)):
        arr.append(int(input(f"Введите значение координат точки {xy[i]}: ")))
    return arr

checkQuarter(inputCoordinatePoint())
