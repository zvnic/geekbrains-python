
# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
import sys

def rangeOfPossibleCoordinates(quarter, maxValue):
    if quarter == 1:
        print(f"{quarter} четверть плоскости диапазон возможных точек (+x,+y) = (0..{maxValue}, 0..{maxValue})")
    if quarter == 2:
        print(f"{quarter} четверть плоскости диапазон возможных точек (-x,+y) = ({-maxValue}..0, 0..{maxValue})")
    if quarter == 3:
        print(f"{quarter} четверть плоскости диапазон возможных точек (-x,-y) = ({-maxValue}..0, {-maxValue}..0)")
    if quarter == 4:
        print(f"{quarter} четверть плоскости диапазон возможных точек (+x,-y) = (0..{maxValue}, {-maxValue}..0)")

maxValue = 100
for i in range(5):
    rangeOfPossibleCoordinates(i, maxValue)