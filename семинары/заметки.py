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