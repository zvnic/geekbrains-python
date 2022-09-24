
# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def inputNumbers():
    xyz = ["X", "Y", "Z"]
    arr = []
    for i in range(len(xyz)):
        arr.append(bool(int(input(f"Введите значение {xyz[i]}: "))))
    return arr

def checkStatement(arr):
    left = not (arr[0] or arr[1] or arr[2])
    right = not arr[0] and not arr[1] and not arr[2]
    result = left == right
    print(f'{left} = {right}')
    return result

value = inputNumbers()

print(value)

if checkStatement(value) == True:
    print('Утверждение истинно')
else:
    print("Утверждение ложно")
