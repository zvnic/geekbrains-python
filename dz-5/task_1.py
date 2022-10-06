"""
Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
"""

def findAndReplaceText(str, word):
    for char in word:
        str = str.replace(char, "")
    return str.replace("  ", " ")

str = input("Введите исходный текст: ")

print(f"Из текста удалены слова содержащие \"абв\": \n {findAndReplaceText(str, 'абв')}")
