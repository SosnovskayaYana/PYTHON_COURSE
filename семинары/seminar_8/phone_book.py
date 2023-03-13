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

# Иванов Иван +79165610080
# Смирнов Сергей +79165610081
# Мосина Ирина +79165610082
# Пушкин Александр +79165610083
# Кашина Светлана +79165610084
# Елесеев Федор +79165610085
# Пушкин Сергей +79165610086
# Есина Татьяна +79165610087
# Есин Олег +79165610088
# Тарасова Ольга +79165610089

def all_contacts():
    with open('семинары/seminar_8/numbers.txt', 'r', encoding='utf8') as data:
        for line in data:
            print(line)

# all_contacts()


def find_contact(contact):
    # contact = contact.upper()
    with open('семинары/seminar_8/numbers.txt', 'r', encoding='utf8') as data:
        for line in data:
            if contact in line:
                print(line)
            # else:
            #     print("Контакт не найден ")

# find_contact(x)


def add_contact(contact):
    with open('семинары/seminar_8/numbers.txt', 'a', encoding='utf8') as data:
        data.write('\n')
        data.write(contact)
        print("Контакт сохранен")

# add_contact()



def main_menu(numb):
    if numb == 1:
        all_contacts()
    elif numb == 2:
        name = input("Введите имя: ")
        find_contact(name.upper())
    elif numb == 3:
        data = input("Введите новый контакт: ")
        add_contact(data.upper())

while True:
    numb = int(input('Введите 1 - для печати всего справочника;'
                ' 2 - для поиска контакта;'
                ' 3 - для записи контакта;'
                ' 4 - для завершения:'))
    if numb == 4:
        break
    main_menu(numb)

