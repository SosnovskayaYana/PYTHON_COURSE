# 1. Дан список чисел. Определите, сколько в нем встречается различных чисел.
# [1, 1, 2, 3, 4, 4] -> 4

# start_list = [1, 1, 2, 3, 4, 4, 7, 7]
# start_set = set(start_list)
# print(len(start_set))






# 2. Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.
# start_list = [1, 2, 3, 4, 5]
# k = 3
# -> [3, 4, 5, 1, 2] = [1, 2, 3, 4, 5]


# start_list = [1, 2, 3, 4, 5]
# k = int(input('Enter K: '))
# k = k % len(start_list)
# result_list = [0, 0, 0, 0, 0]
# i = 0
# while i < len(start_list):
#     if (i + k) >= len(start_list) - 1:
#         result_list[i + k - (len(start_list))] = start_list[i]
#     else:
#         result_list[i + k] = start_list[i]
#     i += 1
# print(result_list)



# staert_list = [1, 2, 3, 4, 5]
# num = 3
# k = num % len(staert_list)
# staert_list_temp = [0]*len(staert_list)  # создали новый список заполненный 0-ми

# for i in range(len(staert_list)):
#     if (i + k) >= len(staert_list): 
#         staert_list_temp[i + k - len(staert_list)] = staert_list[i]
#     else: 
#         staert_list_temp[i + k] = staert_list[i]
# print(staert_list_temp)






# 3. Напишите программу для печати всех уникальных значений в словаре.
# {
#     1: 'Vlad',
#     2: 'Vlad',
#     3: 'Oleg'
# }
# -> 2

# start_dict = {1 : 'Vlad', 2: 'Vlad', 3: 'Oleg'}
# set_end = set()
# for i in start_dict.values():
#     set_end.add(i)
# print(set_end)



# len_dict = len(d)
# list = []
# i = 1

# while i <= len_dict:
#     list.append(d.get(i))   # обращение к ключу
#     i += 1
# list_1 = d.values()   # обращение к элементу
# print(len(set(list_1)))





# 4. Дан массив, состоящий из целых чисел. Напишите программу, 
# которая подсчитает количество элементов массива, больших предыдущего (элемента с предыдущим номером)
# start_list = [3, 7, 1, 7, 1, 4, 9]
# -> 4

# start_list = [3, 7, 1, 7, 1, 4, 9]
# count = 0
# for i in range(1, len(start_list)):
#     if start_list[i - 1] < start_list[i]:
#         count += 1
# print(count)
