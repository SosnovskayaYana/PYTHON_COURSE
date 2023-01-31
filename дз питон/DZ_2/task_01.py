# Задача №1:
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, 
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть.
# Пример:
# 5 -> 1 0 1 1 0

coins = int(input('введите количество монет: '))
coins_list = []

for i in range(coins):
    position = int(input('введите значение: орел -> "0" или решка -> "1": '))
    coins_list.append(position)
# print(coins_list)

count_0 = 0
count_1 = 0

for i in range(len(coins_list)):
    if coins_list[i] == 0:
        count_0 += 1
    else:
        count_1 += 1
# print(f'0 -> {count_0}, 1 -> {count_1}')

if count_1 < count_0:
    print(f'Нужно перевернуть {count_1} монет ')
elif count_0 < count_1:
    print(f'Нужно перевернуть {count_0} монет ')
elif count_0 == count_1:
    print(f'Нужно перевернуть {count_0} монет ')
