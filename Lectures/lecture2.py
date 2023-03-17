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

# Кортеж - неизменяемый список
# t = ()  # создание кортежа
# t = (1, 5, 3, )  # чтобы создать кортеж, оставляем всегда последней запятую в списке

v = [1, 2, 3]
print(v)
print(type(v))

v = tuple(v)  # преобразование списка в кортеж
print(v)
print(type(v))

a, b, c = v
print(a, b, c)
# a, b = 1, 2  # множествнное присваивание, a = 1, b = 2
# a = b = 1
