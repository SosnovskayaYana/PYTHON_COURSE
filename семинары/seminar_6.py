# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод:
# 7
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 
# Вывод:
# 3 3 2 12


# def list_init(el_count: int) -> list:
#     result_list = []
#     for i in range(el_count):
#         num = int(input('num: '))
#         result_list.append(num)
#     return result_list

# n = int(input('n --> '))
# m = int(input('m --> '))

# first_list = list_init(n)
# second_list = list_init(m)

# result = []
# for item in first_list:
#     if item not in second_list:
#         result.append(item)

# print(result)




# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод:
# 5
# 1 2 3 4 
# Ввод:
# 0
# Ввод:
# 5
# 5 1 5 1 5 1
# Вывод: 
# 2


# def list_init(el_count: int) -> list:
#     result_list = []
#     for i in range(el_count):
#         num = int(input('num: '))
#         result_list.append(num)
#     return result_list

# n = int(input('n --> '))
# our_list = list_init(n)
# print(our_list)

# count = 0
# for i in range(1,(len(our_list)-1)):
#     if our_list[i-1] < our_list[i] > our_list[i+1]:
#         count+=1
# print(count)





# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод: 
# 300 220 
# Вывод:
# 284


# def delit(num: int) -> int:
#     result_sum = 0
#     for i in range(1, (num // 2) + 1):
#         if num%i == 0:
#             result_sum += i
#     return result_sum
        
# k = int(input('k: '))
# result = []
# for i in range(2, k + 1):
#     delit_num_1 = delit(i)
#     delit_num_2 = delit(delit_num_1)
#     duet = {i, delit_num_1}
#     if (i == delit_num_2) and (i != delit_num_1) and (duet not in result):
#         result.append(duet)
# print(*result)    убирает лишние скобки
