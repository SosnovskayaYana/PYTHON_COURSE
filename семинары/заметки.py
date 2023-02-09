# тернарный оператор:
# a = int(input('--> '))
# b = 'YES' if ((a % 4 == 0) and (a % 100 != 0)) or (a % 400 == 0) else 'NO'
# print(b)


# моржорый оператор:
# print('YES' if ((a:= int(input('--> '))) % 400 == 0) else 'NO')


# разделитель длинной строки, перенос
# my_str = 'dfghuytre'\
#     '1234'
# print(my_str)


# метод разделения строки сплитом
# num_in_str = '2 2 2 2 3 1'
# print(num_in_str.split(' '))


# метод обьединения строки джоином
# lst = ['wer', '1324', 'sdf']
# print('~~~'.join(lst))


# len() -> возвращает количество элементов в коллекци
# range(5) -> 0, 1, 2, 3, 4
# range(5, 11) -> 5, 6, 7, 8, 9, 10
# range(1, 11, 2) -> 1, 3, 5, 7, 9



# 3. Напишите программу для печати всех уникальных значений в словаре.
# len_dict = len(d)
# list = []
# i = 1
# while i <= len_dict:
#     list.append(d.get(i))   # обращение к ключу
#     i += 1
# list_1 = d.values()   # обращение к элементу
# print(len(set(list_1)))



# .get - метод проверяет есть ли ключ в словаре, если нет, 
# то через запятую передается значение '0'
# если ключ есть, то плюс 1 к счетчику.
# text = input('Введите текст: ')
# d = {}
# for i in text:
#     d[i] = d.get(i,0)+1   
# print(d)



# .isdigit - метод проверяет есть ли ЧИСЛА в пользовательском вводе
# while True:
#     user_text = input('--> ')
#     if not user_text.isdigit(): # if not - возвращает Falce
#         print('игра окончена ')
#         break
# print('Спасибо за игру ')



# Фибаначчи. Рекурсия
# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n-1) + fib(n-2)
# list1 = []
# for i in range(1, 10):
#     list1.append(fib(i))
# print(list1)



# Быстрая сортировка
# def quicksort(array):
#     if len(array) < 2:
#         return array
#     else:
#         pivot = array[0]
#         less = [i for i in array[1:] if i <= pivot]
#         greater = [i for i in array[1:] if i > pivot]
#         return quicksort(less) + [pivot] + quicksort(greater)
# print(quicksort([10, 5, 2, 3]))



# Сортировка слиянием
# def merge_sort(nums):
#     if len(nums) > 1:
#         mid = len(nums) // 2
#         left = nums[:mid]
#         right = nums[mid:]
#         merge_sort(left)
#         merge_sort(right)
#         i = j = k = 0
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 nums[k] = left[i]
#                 i += 1
#             else:
#                 nums[k] = right[j]
#                 j += 1
#             k += 1
#         while i < len(left):
#             nums[k] = left[i]
#             i += 1
#             k += 1
#         while j < len(right):
#             nums[k] = right[j]
#             j += 1
#             k += 1

# list1 = [3, 6, 5, 1, 2, 3, 40, 49, 87, 32, 14]
# merge_sort(list1)
# print(list1)