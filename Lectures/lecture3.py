# Урок 3. Функции, рекурсия, алгоритмы
# Функция — это фрагмент программы, используемый многократно
# Функция начинается с опероатора def

# def sum_numbers(n):
#     summa = 0
#     for i in range(1, n+1):
#         summa += i
#     return summa


# a = sum_numbers(5)
# print(a)

# Напишем функцию, принимающую неограниченное количество аргументов
# c помощью конструкции *args

# Вариант со строковой переменной
# def sum_str(*args):
#     res = ''
#     for i in args:
#         res += i
#     return res


# print(sum_str('h', 'e', 'l', 'l', 'o'))
# print(sum_str('h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd'))

# Вариант с целыми чсилами
# def summa(*args):
#     res = 0
#     for i in args:
#         res += i
#     return res


# print(summa(1, 2, 4))

# МОДУЛЬНОСТЬ

# Создадим отдельный фал с название modul.py и
# после импортируем созданные в нем функции

# import modul1
# print(modul1.max1(5, 9))

# если хотим импортировать абсолютно все функции
# from modul1 import *
# print(max1(5, 9))

# или для импорта конкретной функции
# from modul1 import max1
# print(max1(5, 9))

# можно создать алиас названия модуля

# import modul1 as m1
# print(m1.max1(5, 6))

# ===================================

# РЕКУРСИЯ

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n-1) + fib(n-2)


# list_1 = []
# for i in range(1, 10):
#     list_1.append(fib(i))
# print(list_1)

# АЛГОРИТМЫ СОРТИРОВКИ

# Быстрая сортировка

# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivor = array[0]
#     less = [i for i in array[1:] if i <= pivor]
#     greater = [i for i in array[1:] if i > pivor]
#     return quick_sort(less) + [pivor] + quick_sort(greater)


# print(quick_sort([2, 7, 5, 8]))

# Cортировка слиянием
def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1


list_1 = [1, 5, 7, 3, 2]
merge_sort(list_1)
print(list_1)
