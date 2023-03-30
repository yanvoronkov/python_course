# Задача 39
# Даны два массива чисел. Требуется вывести те элементы первого массива
# (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве.
# Пользователь вводит число N - количество элементов в первом массиве, затем N чисел
# - элементы массива. Затем число M - количество элементов во втором массиве.
# Затем элементы второго массива
# Ввод:
# 7
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1
# Вывод:
# 3 3 2 12

def create_list(list_lengh):
    res_list = []
    for i in range(list_lengh):
        res_list.append(input(f"Введите {i+1} элемент массива: "))
    return res_list


def find_el(list_1, list_2):
    res_list = []
    for i in range(len(list_1)):
        if list_1[i] not in list_2:
            res_list.append(list_1[i])
    return res_list


n = int(input('Введите число элементов массива 1: '))
list_1 = create_list(n)
m = int(input('Введите число элементов массива 2: '))
list_2 = create_list(m)

res_list = find_el(list_1, list_2)
print(res_list)
