
# 1. За день машина проезжает n километров. Сколько дней нужно, 
# чтобы проехать маршрут длиной m километров? При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.

# **Input:**
# n = 700
# m = 750

# **Output:**
# 2

# n = 700
# m = 750
# result = (m + n - 1)//n
# print(result)





# 3. В некоторой школе решили набрать три новых математических класса и 
# оборудовать кабинеты для них новыми партами. 
# За каждой партой может сидеть два учащихся. 
# Известно количество учащихся в каждом из трех классов. 
# Выведите наименьшее число парт, которое нужно приобрести для них.

# **Input:**
# 20
# 21
# 22

# **Output:**
# 32

# n = 20
# m = 21
# s = 22

# #   # result = int((n + m + s) / 2) + 1
# #   # print(result)

# n1 = int(input('Введите количество учеников в 1-ом классе: '))
# n2 = int(input('Введите количество учеников в 2-ом классе: '))
# n3 = int(input('Введите количество учеников в 3-ом классе: '))

# print(f'Требуемое количество парт: {((n1 + 1)//2 + (n2 + 1)//2 + (n3 + 1)//2)}')





# 5. Вагоны в электричке пронумерованы натуральными числами, 
# начиная с 1 (при этом иногда вагоны нумеруются от «головы» поезда, 
# а иногда – с «хвоста»; это зависит от того, в какую сторону едет электричка). 
# В каждом вагоне написан его номер. Витя сел в i-й вагон от головы поезда и обнаружил, 
# что его вагон имеет номер j. Он хочет определить, сколько всего вагонов в электричке. 
# Напишите программу, которая будет это делать или сообщать, 
# что без дополнительной информации это сделать невозможно.

# **Input:**
# 3
# 4

# **Output:**
# 6


# i = int(input('введите: ' ))    # i = int(input('--> ' ))
# j = int(input('введите: ' ))

# if (i == j):
#     print("Витя не сможет посчитать ")
# else:
#     print(i + j - 1, " всего вагонов") 





# 7. Дано натуральное число. 
# Требуется определить, является ли год с данным номером високосным. 
# Если год является високосным, то выведите YES, иначе выведите NO. 
# Напомним, что в соответствии с григорианским календарем, год является високосным, 
# если его номер кратен 4, но не кратен 100, а также если он кратен 400.

# **Input:**
# 2016

# **Output:**
# YES


# year = int(input('--> '))
# if ((year%4 == 0) and (year%100 != 0)) or (year%400 == 0):
#     print('YES')
# else:
#     print('NO')


# year = int(input('--> '))
# result = 'NO'
# if ((year%4 == 0) and (year%100 != 0)) or (year%400 == 0):
#     result = 'YES'
# print(result)

