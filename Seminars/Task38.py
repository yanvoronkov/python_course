# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.


file_path = r'Seminars/text.txt'

def add_record(record):
    with open(file_path, 'a') as f:
        f.write(f"{record}\n")

def read_records():
    with open(file_path, 'r') as f:
        records = f.readlines()
    return records

def search_record(search_record):
    with open(file_path, 'r', encoding='UTF-8') as f:
        for line in f:
            if search_record.casefold() in line.casefold():
                return line.strip()

def replace_record(search_phrase, replace_phrase):
    records = read_records()
    with open(file_path, 'w') as f:
        for record in records:
            if search_phrase in record:
                f.write(replace_phrase + '\n')
            else:
                f.write(record)

def delete_record(search_phrase):
    records = read_records()
    with open(file_path, 'w') as f:
        for record in records:
            if search_phrase not in record:
                f.write(record)


add_record(input('Введите запись: '))
print(''.join(read_records()))
print(search_record(input('Что найти: ')))
replace_record(input('Что заменить: '), input('На что заменить: '))
delete_record(input('Что удалить: '))
