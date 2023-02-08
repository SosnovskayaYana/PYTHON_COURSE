# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

n_set = set()
m_set = set()

n = int(input('Введите количество элементов N: '))
for i in range(n):
    elem = int(input('введите элемент: '))
    n_set.add(elem)

m = int(input('Введите количество элементов M: '))
for i in range(m):
    elem = int(input('введите элемент: '))
    m_set.add(elem)


# n_set = {2, 4, 6, 8, 12, 21, 11, 15, 15, 43, 10}
# m_set = {3, 21, 43, 4, 2, 15, 18}


print(f'N => {n_set}')
print(f'M => {m_set}')

result_set = n_set.intersection(m_set)  # общие элементы множеств
# print(result_set)

num_list = list(result_set)  # преобразование в список
# print(num_list)


sort_num = 0

# while sort_num < len(num_list) - 1:
#     index = 0
#     while (index < len(num_list) - 1 - sort_num):
#         if num_list[index] > num_list[index + 1]:
#             temp = num_list[index]
#             num_list[index] = num_list[index + 1]
#             num_list[index + 1] = temp
#         else:
#             index += 1
    
#     sort_num += 1


for sort_num in range(len(num_list) - 1):
    index = 0

    for index in range(len(num_list) - 1 - sort_num):
        if num_list[index] > num_list[index + 1]:
            temp = num_list[index]
            num_list[index] = num_list[index + 1]
            num_list[index + 1] = temp
        else:
            index += 1
    
    

print(num_list)