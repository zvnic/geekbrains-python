
# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

def calculateLengthDistance(a, b):
    return ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)

def inputCoordinatePoint():
    xy = ["X", "Y"]
    arr = []
    for i in range(len(xy)):
        arr.append(int(input(f"{xy[i]}: ")))
    return arr

print("Введите координаты точки А")
pointA = inputCoordinatePoint()
print("Введите координаты точки В")
pointB = inputCoordinatePoint()

print(f"Длина  расстояния между точками: {format(calculateLengthDistance(pointA, pointB), '.2f')}")