# # создать копию имеющегося списка

values = [1, 4, 5, 'asf', 2.323, True]
result = list(map(lambda list_item: list_item, values))

if result == values:
    print('ok')
else:
    print('not ok')



# result = [1, 5, 7, 3, 7]
# new_list_1 = list(map(lambda num: num*num, result))
# # что сделать где взять при каком условии  list conprehencion
# new_list_2 = [item*item for item in result if item > 4]
# print(new_list_1)
# print(new_list_2)






# Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту, орбита которой имеет самую большую площадь. 
# Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит планет найдет ту, по которой вращается самая далекая 
# планета. Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет, зато искусственные спутники были были запущены 
# на круговые орбиты. Результатом функции должен быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты. Каждая орбита 
# представляет из себя кортеж из пары чисел - полуосей ее эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины 
# полуосей эллипса. При решении задачи используйте списочные выражения. Подсказка: проще всего будет найти эллипс в два шага: сначала 
# вычислить самую большую площадь эллипса, а затем найти и сам эллипс, имеющий такую площадь. Гарантируется, что самая далекая планета 
# ровно одна


# def find_farthest_orbit_1(list_of_orbits: list[tuple]) -> tuple:   # приняли список кортежей и вернули кортеж
#     func_list_orbits = list_of_orbits.copy()   # создали копию входного листа
#     func_list_orbits = list(filter(lambda orbits: orbits[0] != orbits[1], func_list_orbits))   # отфильтровали круглые орбиты
#     s_orbits = tuple(map(lambda orbits: orbits[0]*orbits[1], func_list_orbits))    # перемножили элементы и записали в нов. кортеж
#     max_orbits = max(s_orbits)   # нашли мах элемент
#     index_max_s = s_orbits.index(max_orbits)    # в новую переменную записали индекс мах элемента
#     return func_list_orbits[index_max_s]   # вернули элемент списка с мах площадью


# def find_farthest_orbit_2(list_of_orbits: list[tuple]):
#     s_orbit = {(orbita[0]*orbita[1]): orbita for orbita in list_of_orbits if orbita[0] != orbita[1]}
#     return s_orbit[max(s_orbit)]
# # решение через лист конперхэйшн. создали словарь, в него положили S-площадь в виде ключа и орбиты в виде объекта.
# # выборку делали из  list_of_orbits  не учитывая элементы с одинаковыми полуорбитами. вернули через мах функцию элемент с мах ключем.


# def find_farthest_orbit_3(list_of_orbits: list[tuple]):
#     s_orbits = tuple(map(lambda orbits: orbits[0]*orbits[1] if orbits[0] != orbits[1] else 0, list_of_orbits))
#     # перемножили элементы и записали в нов. кортеж, если полуарбиты не равны, иначе запишет 0
#     max_orbits = max(s_orbits)
#     index_max_s = s_orbits.index(max_orbits)
#     return list_of_orbits[index_max_s]


# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]


# print(*find_farthest_orbit_1(orbits))
# print(*find_farthest_orbit_2(orbits))
# print(*find_farthest_orbit_3(orbits))






# Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение 
# некоторой характеристики, и возвращают True, если это так. Если значение характеристики для разных объектов отличается 
# - то False. Для пустого набора объектов, функция должна возвращать True. Аргумент characteristic - это функция, 
# которая принимает объект и вычисляет его характеристику.
# Ввод: 
# values = [0, 2, 10, 6]
# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')
# Вывод:
# same
      

# def same_by(characteristic, objects):
#     if objects:
#         return len(set(map(characteristic, objects))) == 1
#     return True

# values = [0, 2, 10, 6]

# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')
