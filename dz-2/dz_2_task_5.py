"""
5. Реализуйте алгоритм перемешивания списка.
"""
import random

def mix_list(list_original):
    list_res = list_original
    for i in range(len(list_res)):
        indexRandom = random.randint(0, len(list_res) - 1)
        temp = list_res[i]
        list_res[i] = list_res[indexRandom]
        list_res[indexRandom] = temp
    return list_res

listNums = [i for i in range(1, 10)]
print(f"Исходный список:     {listNums}")
print(f"Перемешанный список: {mix_list(listNums)}")
