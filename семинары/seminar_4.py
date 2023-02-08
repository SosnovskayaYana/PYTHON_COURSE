# 1. Напишите программу, которая принимает на вход строку, и отслеживает,
# сколько раз каждый символ уже встречался.
# 'Hello, World!'
# H: 1
# e: 1


# our_string = 'Hello, world!'
# our_dict = {}
# count_list = set(our_string)
# for letter in count_list:
#     count_letter = 0
#     for letter_in_word in our_string:
#         if letter == letter_in_word:
#             count_letter+=1
#     our_dict[letter] = count_letter
# print(our_dict)




# start_list = input('Введите любую строку: ')
# count = 0
# start_set = set(start_list)
# uniq_list = list(start_set)
# new_dict = dict()

# for i in range(len(uniq_list)):

#     for j in range(len(start_list)):
#         if uniq_list[i] == start_list[j]:
#             count += 1

#     new_dict[uniq_list[i]] = count
#     count = 0
    
# print(new_dict)




# text = input('Введите текст: ')
# d = {}
# for i in text:
#     d[i] = d.get(i,0)+1
# print(d)






# 2. Пользователь вводит текст(строка). Словом считается последовательность непробельных 
# символов идущих подряд, слова разделены одним или большим числом пробелов.Определите, сколько различных 
# слов содержится в этом тексте.
# 'qwrqw  qwr g,l;c wet 234      3dgs'
# -> 6


# text = input('Введите текст: ')
# list_text = text.split()
# print(len(list_text))






# 3. Ваня и Петя поспорили, кто быстрее решит следующую задачу: 
#     “Задана последовательность неотрицательных целых чисел. 
#     Требуется определить значение наибольшего элемента последовательности, 
#     которая завершается первым встретившимся нулем (число 0 не входит в последовательность)”. 
#     Однако 2 друга оказались не такими смышлеными. Никто из ребят не смог до конца сделать это задание.
#     Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор. 
#     За помощью товарищи обратились к Вам, студентам.
    
# 2
# 4
# 6
# 2
# 8
# 0
# -> 8


# num = int(input('Введите число: '))
# max_num = num
# while num != 0:
#     if num > max_num:
#         max_num = num
#     num = int(input('Введите число: '))
# print(f'максимальное число: {max_num}')



# print('Вводим числа')
# number = None
# array = list()
# while number != 0:
#     number = int(input('Введите число: '))
#     array.append(number)
# print(f'максимальное число: {max(array)}')



# my_str = []
# while True:
#   n = int(input('Введите число: '))
#   my_str.append(n)
#   if n == 0:
#     break
# print(my_str)
# max_number = 0
# for elem in my_str:
#     if elem > max_number:
#         max_number = elem
# print(max_number)
