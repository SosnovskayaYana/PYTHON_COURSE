# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X

# 5
# 1 2 3 4 5
# 6
# -> 5

n = int(input('введите количество элементов: '))
a = []

for i in range(n):
    elem = int(input('введите элемент: '))
    a.append(elem)
print(a)

x = int(input('введите X: '))

# a = [2, -5, 7, 6, 20]
# x = -30

res = 0
res_elem = 999999999
x_element = 0

for i in range(len(a)):

    if a[i] <= x:
        res = x - a[i]
        if res < res_elem:
            res_elem = res
            x_element = a[i]
        else:
            i += 1

    elif a[i] > x:
        res = a[i] - x
        if res < res_elem:
            res_elem = res
            x_element = a[i]
        else:
            i += 1

print(f'Самый близкий по величине элемент к заданному X: {x_element}')