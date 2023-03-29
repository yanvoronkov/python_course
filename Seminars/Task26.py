# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

# def pow_num(a, b):
#     pow_num = a
#     for i in range(1, b):
#         pow_num = pow_num * a
#     return pow_num


def find_pow(a, b):
    if b == 1:
        return a
    else:
        return (a*find_pow(a, b-1))


a = int(input('Введите число: '))
b = int(input('Введите степень числа: '))
print(find_pow(a, b))
