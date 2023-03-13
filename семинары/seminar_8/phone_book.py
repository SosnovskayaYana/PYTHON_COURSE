# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, 
# номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

# 1. Вывод всех контактов
# 2. Поиск контакта
# 3. Добавить контакт (сразу сохрорнять в файл)
# 4. Выход по требованию пользователя


text_file = 'семинары/seminar_8/numbers.txt'  # путь к текстовому файлу указан в переменной


def all_contacts():
    with open(text_file, 'r', encoding='utf8') as data:
        for line in data:
            print(line)
# all_contacts()


def find_contact(contact):
    # contact = contact.upper()
    with open(text_file, 'r', encoding='utf8') as data:
        for line in data:
            if contact in line:
                print(line)
            # else:
            #     print("Контакт не найден ")
# find_contact('')


def add_contact(contact):
    with open(text_file, 'a', encoding='utf8') as data:
        # data.write('\n')
        # data.write(contact)
        data.write('\n' + contact)
        print("Контакт сохранен")
# add_contact('')


def del_contact(contact):
    with open(text_file, 'r', encoding='utf8') as data:
        new_text = []
        for line in data:
            if contact not in line:
                new_text.append(line)
            else:
                continue

    with open(text_file, 'w', encoding='utf8') as data:
        data.writelines(new_text)
        print('Данные удалены ')   
# del_contact('СЕРГЕЙ')


def change_contact(contact):
    with open(text_file, 'r', encoding='utf8') as data:
        new_text = []
        for line in data:
            if contact in line:
                x = input(f"{line} -> Введите новые данные или прежние: ").upper()
                new_text.append(x + '\n')
            else:
                new_text.append(line)
    
    with open('семинары/seminar_8/numbers.txt', 'w', encoding='utf8') as data:
        data.writelines(new_text)
        print('Данные изменены ')
# change_contact('ОЛЕГ')


def main_menu(number):
    if number == 1:
        all_contacts()
    elif number == 2:
        name = input("Введите данные для поиска: ")
        find_contact(name.upper())
    elif number == 3:
        data = input("Введите новый контакт: ")
        add_contact(data.upper())
    elif number == 5:
        data = input("Введите данные для удаления: ")
        del_contact(data.upper())
    elif number == 6:
        data = input("Введите данные для изменения: ")
        change_contact(data.upper())

while True:
    number = int(input('Введите:\n'
                ' 1 - для печати всего справочника;\n'
                ' 2 - для поиска контакта;\n'
                ' 3 - для записи контакта;\n'
                ' 4 - для завершения программы;\n'
                ' 5 - для удаления контакта;\n'
                ' 6 - для изменения контакта;\n'
                ' ->  '))
    if number == 4:
        break
    main_menu(number)


# def copy_contacts():
#     with open(text_file, 'r', encoding='utf8') as data:
#         new_text = []
#         for line in data:
#             new_text.append(line)
#         return new_text

# with open('семинары/seminar_8/phones.txt', 'w', encoding='utf8') as data:
#     data.writelines(copy_contacts())
#     print('ok')


