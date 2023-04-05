# Задача №49. Общее обсуждение
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

file_path = r'Seminars/text.txt'


def read_app():
    with open(file_path, 'r', encoding='UTF-8') as f:
        print(f.read())


def append_app():
    with open(file_path, 'a', encoding='UTF-8') as f:
        f.write('\n'+input())


def find_app():
    temp = input('Введите слово для поиска: ')
    with open(file_path, 'r', encoding='UTF-8') as f:
        for line in f:
            if temp.casefold() in line.casefold():
                print(line.strip())


append_app()
read_app()
# find_app()
