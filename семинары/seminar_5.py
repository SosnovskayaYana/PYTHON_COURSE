# 1. Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи

# num = int(input('Введите число: '))
# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n-1)+ fib(n-2)
# list1 = []
# for i in range (1, num+1):
#    list1.append(fib(i))
# print(list1)


# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n in [1, 2]:
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)
# n = int(input('--> '))
# result = fibonacci(n)
# print(result)





# 2. Хакер Василий получил доступ к классному журналу и хочет заменить все свои 
# минимальные оценки на максимальные. Напишите программу, 
# которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# [4, 2, 2, 1, 5, 5]

# list1 = [4, 2, 2, 1, 5, 5] 
# for i in range(len(list1)):
#     if list1[i] == 5 or list1[i] == 4:
#         list1[i] = 2
# print(list1)


# def replace_marks(marks_list: list) -> list:   #тайпхитинг
#     for i in range(len(marks_list)):
#         if (marks_list[i] == 5) or (marks_list[i] == 4):
#             marks_list[i] = 2
#     return marks_list
# marks = [4, 2, 2, 1, 5, 5]
# print(replace_marks(marks))


# def swapmark(n):
#     if n == 5:
#         return 1
#     elif n == 4:
#         return 2
#     else:
#         return n
# marks = [4, 2, 2, 1, 5, 5]
# for i in range(len(marks)):
#     marks[i] = swapmark(marks[i])
# print(marks)





# 1. Напишите функцию, которая принимает одно число и проверяет, является ли оно простым

# def test(num):
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True
# n = int(input("Введите число: "))
# print(test(n))


# def natural_num(num):
#     for i in range(2, num%2):
#         if num % i == 0:
#             return True
#             # print(f'Введенное число {num} не является простым')
#     return False
#         # else:
#         #     print(f'Введенное число {num} является простым')
# number = int(input('Введите число: '))
# print(natural_num(number))





# 2. Дано натуральное число N и последовательность из N элементов. 
# Требуется вывести эту последовательность в обратном порядке

# def revers_nums(n):
#     if n == 0:
#         return ''
#     k = input('--> ')
#     return revers_nums(n - 1) + k

# print(revers_nums(4))
