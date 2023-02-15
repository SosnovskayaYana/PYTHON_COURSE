# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону (т.е. не меньше заданного 
# минимума и не больше заданного максимума)

# max_elem_range = 20
# min_elem_range = 10

n = int(input('Введите количество элементов: '))
list_1 = [(int(input('Введите число: '))) for i in range(n)]
print(list_1)

min_elem_range = int(input('Введите нижний порог: '))
max_elem_range = int(input('Введите верхний порог: '))

list_2 = []

for i in range(len(list_1)):
    if list_1[i] >= min_elem_range and list_1[i] <= max_elem_range:
        list_2.append(i)

print(list_2)