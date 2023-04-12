'''Скрипты для выполнения операций'''
from data_create import name_data, surname_data
from data_create import phone_data, address_data


def change_data_list(num, list):
    '''Замена строки с данными пользователя для 3-й команды'''
    while num < 1 or num > 4:
        num = int(input("Введите число от 1 до 4: "))
    if num == 1:
        list[0] = name_data()
    elif num == 2:
        list[1] = surname_data()
    elif num == 3:
        list[2] = phone_data()
    else:
        list[3] = address_data()
    return list


def input_data():
    '''Ввод данных'''
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()

    var = int(input(f"В каком формате Вы хотите записать данные?\n\n"
                    f"1 Вариант:\n\n"
                    f"{name}\n"
                    f"{surname}\n"
                    f"{phone}\n"
                    f"{address}\n\n"
                    f"2 Вариант:\n\n"
                    f"{name};{surname};{phone};{address}\n\n"
                    f"Выберите номер варианта: "))

    while var != 1 and var != 2:
        print('Нужно выбрать номер 1 или номер 2')
        print('Введите номер варианта')
        var = int(input("Введите номер варианта: "))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name}\n{surname}\n{phone}\n{address}\n\n')
    else:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{address}\n\n')


def delete_data():
    '''Удаление записи пользователя'''
    print('Из какого файла Вы хотите удалить данные?')
    data_first, data_second = print_data()

    number_file = int(input('Введите номер файла: '))

    while number_file not in (1, 2):
        print("Нужно выбрать номер 1 или номер 2\n"
              "Введите номер варианта")
        number_file = int(input('Введите номер файла: '))

    print("Какую именно запись по счету Вы хотите удалить?")

    # Блок для первого файла
    if number_file == 1:

        # Выводится нумерованный список строк с записями
        for i in range(1, len(data_first)+1):
            print(f"{i}: {data_first[i-1]}")

        number_journal = int(input('Введите номер записи: '))
        while number_journal < 1 or number_journal > len(data_first):
            number_journal = int(
                input(f"Введите пожалуйста число от 1 до {len(data_first)}: "))

        print(
            f"Вы хотите удалить данные пользователя:\n"
            f"{data_first[number_journal - 1]}"
        )

        # Подтверждение удаления
        valid = input("Введите 1 для подтверждения: ")
        if valid == '1':
            print("Запись удалена")
            with open('data_first_variant.csv', 'w', encoding='utf-8')\
                    as file:
                file.write(f"{''.join(data_first[:number_journal - 1])}")
                file.write(f"{''.join(data_first[number_journal:])}")
        else:
            print("Удаление отменено")
    # Блок для второго файла
    else:
        # Выводится нумерованный список строк с записями
        for j in range(1, len(data_second) + 1):
            print(f'{j}. {data_second[j-1]}')

        number_journal_2 = int(input('Введите номер записи: '))
        while (number_journal_2 < 1 or number_journal_2 >
               len(data_second)):
            number_journal_2 = int(
                input(f"Введите пожалуйста число от 1 до"
                      f"{len(data_second)}: "))
        print(
            f"Вы хотите удалить данные пользователя:\n"
            f"{data_second[number_journal_2 - 1]}")

        # Подтверждение удаления
        valid = input("Введите 1 для подтверждения: ")
        if valid == '1':
            print("Запись удалена")
            with open('data_second_variant.csv', 'w', encoding='utf-8')\
                    as file:
                file.write(f"{''.join(data_second[:number_journal_2 - 1])}")
                file.write(f"{''.join(data_second[number_journal_2:])}")
        else:
            print("Удаление отменено")


def change_data():
    '''Замена записи'''
    print('Из какого файла Вы хотите изменить данные?')
    data_first, data_second = print_data()

    number_file = int(input('Введите номер файла: '))
    while number_file not in (1, 2):
        print('Нужно выбрать номер 1 или номер 2')
        print('Введите номер варианта')
        number_file = int(input('Введите номер файла: '))

    print("Какую именно запись по счету Вы хотите изменить?")

    # Блок для первого файла
    if number_file == 1:
        for i in range(1, len(data_first)+1):
            print(f"{i}: {data_first[i-1]}")

        number_journal = int(input('Введите номер записи: '))
        while number_journal < 1 or number_journal > len(data_first):
            number_journal = int(
                input(f"Введите пожалуйста число от 1 до {len(data_first)}: "))

        print(
            f"Вы хотите изменить данные пользователя:\n"
            f"{data_first[number_journal - 1]}")
        changed_list = []
        str_1 = ""
        j = 0
        for i in range(len(data_first[number_journal - 1])-1):
            if data_first[number_journal - 1][i] == "\n":
                changed_list.append(str_1)
                j = i + 1
            else:
                str_1 = ''.join(data_first[number_journal - 1][j:i+1])

        change_data_num = int(input(
            "Какие данные вы хотите изменить?\nВведите 1 - имя,"
            "2 - Фамилия, 3 - телефон, 4 - адрес: "))

        changed_list = change_data_list(change_data_num, changed_list)
        print(changed_list)

        changed_list = ['\n'.join(changed_list) + '\n\n']
        with open('data_first_variant.csv', 'w', encoding='utf-8')\
                as file:
            file.write(f"{''.join(data_first[:number_journal - 1])}")
            file.write(f"{''.join(changed_list)}")
            file.write(f"{''.join(data_first[number_journal:])}")

    # Блок для второго файла
    else:
        for j in range(1, len(data_second) + 1):
            print(f'{j}. {data_second[j-1]}')

        number_journal_second = int(input('Введите номер записи: '))
        while (number_journal_second < 1 or number_journal_second >
               len(data_second)):
            number_journal_second = int(
                input(f"Введите пожалуйста число от 1 до"
                      f"{len(data_second)}: "))

        print(
            f"Вы хотите изменить данные пользователя:\n"
            f"{data_second[number_journal_second-1]}")

        changed_second_list = []
        j = 0
        for i, num in enumerate(data_second[number_journal_second-1]):
            if num == ";" or i == len(data_second[number_journal_second-1])-2:
                changed_second_list.append(
                    ''.join(data_second[number_journal_second-1][j:i]))
                j = i + 1

        change_second_data_num = int(input(
            "Какие данные вы хотите изменить?\n"
            "Введите 1 - имя, 2 - Фамилия,"
            " 3 - телефон, 4 - адрес: "))

        # Вызов функции замены данных в записи
        changed_second_list = change_data_list(change_second_data_num,
                                               changed_second_list)

        changed_second_list = ';'.join(changed_second_list) + "\n\n"

        with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
            file.write(f"{''.join(data_second[:number_journal_second-1])}")

            file.write(f"{changed_second_list}")

            file.write(f"{''.join(data_second[number_journal_second:])}")


def print_data():
    '''Вывод данных'''
    print('Вывожу данные для Вас из 1-ого файла\n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data_first = file.readlines()
        data_first_version_second = []
        j = 0
        for i, num in enumerate(data_first):
            if num == '\n' or i == len(data_first) - 1:
                data_first_version_second.append(''.join(data_first[j:i + 1]))
                j = i + 1
        data_first = data_first_version_second
        print(''.join(data_first))
        # print(*data_first, sep='')
    print('Вывожу данные для Вас из 2-ого файла\n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data_second = file.readlines()
        data_second_version_second = []
        j = 0
        for i, num in enumerate(data_second):
            if num == '\n' or i == len(data_second) - 1:
                data_second_version_second.append(
                    ''.join(data_second[j:i + 1]))
                j = i + 1
        data_second = data_second_version_second
        print(''.join(data_second))
    return data_first, data_second
