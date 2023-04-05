# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
#     **Вывод:** Парам пам-пам


def find_vowels(vowels, phrase):
    count = 0
    for letter in phrase:
        if letter.lower() in vowels:
            count += 1
    return count


def check_words(phrase):
    phrase_new = phrase.split()
    sum = 0
    for i in range(len(phrase_new)):
        sum += find_vowels(vowels, phrase_new[i])
    if sum % len(phrase_new) == 0:
        print('“Парам пам-пам”')
    else:
        print('“Пам парам”')


vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
phrase = input('Введите стихотворение: ')
check_words(phrase)


# def rhythm(song):
#     vowels = list(map(lambda x: len([letter for letter in x if letter in ('а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я')]), song.split()))
#     return all(x == vowels[0] for x in vowels)


# my_song = input("Введите песню: ")
# if rhythm(my_song):
#     print("Парам пам-пам")
# else:
#     print("Пам парам")
