# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

import os


def print_data():
    with open("phonebook.txt", "r", encoding="utf-8") as file:
        phonebook_str = file.read()
    print(phonebook_str)
    print()


def input_name():
    return input("Введите имя контакта: ").title()


def input_surname():
    return input("Введите фамилию контакта: ").title()


def input_patronymic():
    return input("Введите отчество контакта: ").title()


def input_phone():
    return input("Введите номер телефона контакта: ")


def input_address():
    return input("Введите аадрес контакта: ").title()


def input_data():
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    my_sep = " "
    return f"{surname}{my_sep}{name}{my_sep}{patronymic}{my_sep}{phone}\n{address}\n\n"


def add_contact():
    new_contact_str = input_data()
    with open("phonebook.txt", "a", encoding="utf-8") as file:
        file.write(new_contact_str)


def search_contact():
    print("Варианты поиска:\n"
          "1.По фамилии\n"
          "2.По имени\n"
          "3.По отчеству\n"
          "4.По телефону\n"
          "5.По адресу\n")
    command = input("Выберите вариант поиска: ")

    while command not in ("1", "2", "3", "4", "5"):
        print("Некоректные ввод повториет запрос ")
        command = input("Выберите вариант поиска: ")

    i_search = int(command) - 1
    search = input("Введите данные для поиска: ").lower()
    print()

    with open("phonebook.txt", "r", encoding="utf-8") as file:
        contacts_list = file.read().rstrip().split("\n\n")

    check_cont = False
    for contact_str in contacts_list:
        lst_contact = contact_str.lower().replace("\n", " ").split()
        if search in lst_contact[i_search]:
            print(contact_str)
            print()
            check_cont = True

    if not check_cont:
        print("Такого контакта нет.")


def read_file(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        info_from_file = f.read().lower()
    list_result = []
    for line in info_from_file.split("\n\n"):
        if line != '':
            name_and_number = line.split("\n")[0].split(" ")
            city = line.split("\n")[1]
            name_and_number.append(city)
            list_result.append(name_and_number)
    return list_result


def changes_contact():
    file_name = "phonebook.txt"
    enter_users = input("введите фамилию или имя или отчество контакта: ").lower()
    dict_phone_number = read_file(file_name)
    row_number = search_in_list(dict_phone_number, enter_users)
    if row_number is None:
        print("Не удалось найти запись")
        return
    print("Варианты изминения:\n"
          "1.По фамилии\n"
          "2.По имени\n"
          "3.По отчеству\n"
          "4.По телефону\n"
          "5.По адресу\n")
    enter_users = input("Выберите пункт: ")
    if enter_users not in ("1", "2", "3", "4", "5"):
        print("Некоректные ввод повториет запрос ")
        return
    else:
        changes_index = int(enter_users) - 1
    new_data = input("Введите новые данные: ")
    change_list = change_data(dict_phone_number, row_number, changes_index, new_data)
    write_file(file_name, change_list)


def search_in_list(info, key_search):
    for row in range(0, len(info) - 1):
        for column in range(0, len(info[row]) - 1):
            if info[row][column] == key_search:
                return row
    return None


def write_file(file_name, change_list):
    result_str = ""
    for row in change_list:
        if row[0] != "":
            result_str += " ".join(row[:4]) + "\n"
            result_str += row[4] + "\n\n"
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(result_str.title())


def change_data(info, row_number, changes_index, new_data):
    info[row_number][changes_index] = new_data
    return info


def remove_data(info, row_number):
    info.pop(row_number)
    return info


def delete_contact():
    file_name = "phonebook.txt"
    dict_phone_number = read_file(file_name)
    enter_users = input("введите фамилию или имя или отчество контакта: ").lower()
    row_number = search_in_list(dict_phone_number, enter_users)
    if row_number is None:
        print("Не удалось найти запись")
        return
    new_dict_phone_number = remove_data(dict_phone_number, row_number)
    write_file(file_name, new_dict_phone_number)


def interface():
    with open("phonebook.txt", "a", encoding="utf-8"):
        pass
    command = ""
    os.system("cls")
    while command != "6":
        print("Меню пользователя:\n"
              "1.Вывод данных на экран\n"
              "2.Добавить контакт\n"
              "3.Поиск контакта\n"
              "4.Изменть контакт\n"
              "5.Удалить контакт\n"
              "6.Выход\n")
        command = input("Выбериет пункт меню: ")

        while command not in ("1", "2", "3", "4", "5", "6"):
            print("Некоректные ввод повториет запрос ")
            command = input("Ввыбериет пункт меню ")
        match command:
            case "1":
                print_data()
            case "2":
                add_contact()
            case "3":
                search_contact()
            case "4":
                changes_contact()
            case "5":
                delete_contact()
            case "6":
                print("Завершение программы")
        print()

if __name__ == "__main__":
    interface()
