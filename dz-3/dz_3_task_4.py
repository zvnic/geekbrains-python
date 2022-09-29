"""
4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10
"""

def decimalToBinary(num):
    binaryString = ""
    while num != 0:
        binaryString = str(num%2) + binaryString
        num //= 2
    return binaryString

numbers = int(input("Введите десятичное число для преобразовывания в двоичное: "))

print(f"{numbers} -> {decimalToBinary(numbers)}")