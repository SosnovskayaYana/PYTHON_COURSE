# Задача 1
# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

num_a = int(input('Введите число A: '))
num_b = int(input('Введите целую степень B: '))


def degree(a, b):
    if b == 1:
        return a
    return a * degree(a, b-1)

print(degree(num_a, num_b))



# def degree(a, b):
#     if b == 1:
#         return a
#     return degree(a*a, b-1)  # неверно!!!!
# print(degree(num_a, num_b))


# решение без рекурсии
# def degree1(a, b):
#     count = 1
#     res = 1
#     while count <= b:
#         res = res * a
#         count += 1
#     return res
# print(degree1(num_a, num_b))

