# Задача №45. Решение в группах
# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 10^5
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод:
# 300
# Вывод:
# 220 284


def find_sum_div(num):
    sum_div = 0
    for i in range(1, num):
        if num % i == 0:
            sum_div += i
    return sum_div


input_num = int(input('Введите число: '))
for num_1 in range(2, input_num + 1):
    num_2 = find_sum_div(num_1)
    sum_num_2 = find_sum_div(num_2)
    if (sum_num_2 == num_1) and (num_1 < num_2):
        print(num_1, num_2)


# Решение 2

# def sum_divide(number):

#     sum_divide, i = 1, 2las

#     while i*i < number:
#         if number % i == 0:
#             sum_divide += i
#             sum_divide += (number//i)
#         i += 1

#     return sum_divide


# k, i = 100000, 1
# while i < k:
#     j = sum_divide(i)
#     if i < j < k and i == sum_divide(j):
#         print(f'{i} {j}')
#     i += 1

# Решение 3


# def sum_num(k):
#     sum1 = 0
#     for i in range(1, (k // 2) + 1):
#         if k % i == 0:
#             sum1 += i
#     return sum1


# k = int(input('Введите число: '))
# for i in range(1, k):
#     j = sum_num(i)
#     if i < j <= k and i == sum_num(j):
#         print(i, j)
