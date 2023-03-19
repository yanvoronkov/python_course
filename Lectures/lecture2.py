# list_1 = []
# list_1 = list()
# list_1 = [1, 2, 3, 4, 5]
# print(list_1)
# print(*list_1)  # звездочка убирает все знаки (скобки, запятые)

# for i in list_1:
#     print(i)


# print(len(list_1))
# print(list_1[0])
# print(list_1[-2])

# Добавление значений в список

# print(list_1)
# list_1.append(8) #append добавляет в конец списка новый элемент, указанный в скобках
# print(list_1)

# list_1 = []
# print(list_1)
# for i in range(5):
#     list_1.append(i)
#     print(list_1)


# list_1 = [1, 2, -3, 21, 0]
# print(list_1.pop())  # pop удаляет из списка последний элемент и возвращает его
# print(list_1)

# удаление конкретного элемента из списка
# list_1 = [1, 2, -3, 21, 0]
# # pop удаляет из списка элемент c заданным индексом и возвращает его
# print(list_1.pop(2))
# print(list_1)

# добавление элемента на нужную позицию
# list_1 = [1, 2, -3, 21, 0]
# # insert добавляет в список элемент на позицию с индексом (первое число) и занчением (второе число)
# print(list_1.insert(2, 11))
# print(list_1)

# # обращение к элементам списка
# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list_1[0])
# print(list_1[-1])
# print(list_1[-5])
# print(list_1[:])
# print(list_1[:2])
# print(list_1[len(list_1) - 2:])
# print(list_1[6:-2])
# print(list_1[0:len(list_1) - 2:2])

# КОРТЕЖ - неизменяемый список

# t = ()  # создание кортежа
# t = (1, 5, 3, )  # чтобы создать кортеж, оставляем всегда последней запятую в списке

# v = [1, 2, 3]
# print(v)
# print(type(v))

# v = tuple(v)  # преобразование списка в кортеж
# print(v)
# print(type(v))

# a, b = 1, 2  # множествнное присваивание, a = 1, b = 2
# a = b = 1

# распаковка кортежа
# v = (1, 2, 3,)
# a, b, c = v
# print(a, b, c)

# работа с кортежем
# t = (1, 2, 3, )
# print(t[2])
# for i in t:
#     print(i)
# for i in range(len(t)):
#     print(t[i])


# СЛОВАРИ

# d = {}
# d = dict()

# d['q'] = 'qwerty'
# print(d)
# d['w'] = 'werty'
# print(d)
# print(d['q'])

# dictionary = {}
# dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary)  # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left'])  # ←
# # типы ключей могут отличаться
# print(dictionary['up'])  # ↑
# # типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left'])  # ⇐
# # print(dictionary['type'])  # KeyError: 'type'
# # del dictionary['left']  # удаление элемента
# for item in dictionary:
#     print('{}: {}'.format(item, dictionary[item]))
# # up: ↑
# # down: ↓
# # right: →
# for (k, v) in dictionary.items():
#     print(k, v)


# МНОЖЕСТВА

# colors = {'red', 'green', 'blue'}
# print(colors)  # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors)  # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors)  # {'red', 'green', 'blue','gray'}
# colors.remove('red')
# print(colors)  # {'green', 'blue','gray'}
# # colors.remove('red')  # KeyError: 'red'
# colors.discard('red')  # ok
# print(colors)  # {'green', 'blue','gray'}
# colors.clear()  # { }
# print(colors)  # set()

# q = set()  # создание путого множества

# операции со множествами
# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()  # c = {1, 2, 3, 5, 8}
# u = a.union(b)  # u = {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b)  # i = {8, 2, 5}
# dl = a.difference(b)  # dl = {1, 3}
# dr = b.difference(a)  # dr = {13, 21}
# q = a.union(b).difference(a.intersection(b))  # {1, 21, 3, 13}

# Неизменяемое или замороженное множество(frozenset) — множество, с которым
# не будут работать методы удаления и добавления.
# a = {1, 2, 3, 5, 8}
# b = frozenset(a)
# print(b)  # frozenset({1, 2, 3, 5, 8})


# List Comprehension
# У каждого языка программирования есть свои особенности и преимущества. Одна
# из культовых фишек Python — list comprehension(редко переводится на русский, но
#                                                можно использовать определение «генератора списка»). Comprehension легко
# читать, и их используют как начинающие, так и опытные разработчики.

# List comprehension — это упрощенный подход к созданию списка, который
# задействует цикл for, а также инструкции if-else для определения того, что в итоге
# окажется в финальном списке.


# Задача: Создать список, состоящий из четных чисел в диапазоне от 1 до 100.
# Решение:
# 1. Создать список чисел от 1 до 100

# list_1 = []
# for i in range(1, 101):
#     list_1.append(i)
# print(list_1)  # [1, 2, 3,..., 100]

# Эту же функцию можно записать так:
# list_1 = [i for i in range(1, 101)]  # [1, 2, 3,..., 100]
# print(list_1)

# 2. Добавить условие (только чётные числа)
# list_1 = [i for i in range(1, 101) if i % 2 == 0]  # [2, 4, 6,..., 100]
# print(list_1)

# Допустим, вы решили создать пары каждому из чисел (кортежи)
# list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0]  # [(2, 2), (4, 4),...,(100, 100)]
# print(list_1)

# Также можно умножать, делить, прибавлять, вычитать. Например, умножить
# значение на 2.

# list_1 = [i * 2 for i in range(10) if i % 2 == 0]
# print(list_1)  # [0, 4, 8, 12, 16]


# Профилирование и отладка
# Мы с вами люди, а людям суждено ошибаться, даже при написании программного
# кода 🙂
# Давайте разберем с Вами самые частые ошибки в написании кода на Python.
# 🔥 Самые распространенные ошибки:

# # ● SyntaxError(Синтаксическая ошибка)
# number_first = 5
# number_second = 7
# if number_first > number_second  # !!!!!
# print(number_first)

# # ● IndentationError(Ошибка отступов)
# number_first = 5
# number_second = 7
# if number_first > number_second:
# print(number_first)  # !!!!!

# ● TypeError(Типовая ошибка)
# text = 'Python'
# number = 5
# print(text + number)
# # Нельзя складывать строки и числа

# ● ZeroDivisionError(Деление на 0)
# number_first = 5
# number_second = 0
# print(number_first // number_second)
# # Делить на 0 нельзя

# ● KeyError(Ошибка ключа)
# dictionary = {1: 'Monday', 2: 'Tuesday'}
# print(dictionary[3])
# # Такого ключа не существует

# ● NameError(Ошибка имени переменной)
# name = 'Ivan'
# print(names)
# # Переменной names не существует

# ● ValueError(Ошибка значения)
# text = 'Python'
# print(int(text))
# # Нельзя символы перевести в целые значения
