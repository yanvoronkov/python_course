# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

# number_of_bushes = (int(input('Введите количество кустов: ')))
# dict_of_bushes = {}
# for i in 3:
#     dict_of_bushes[i] = int(input(f"Введите количество ягод на кусте {i+1}: "))
# max_harvest = 0
# for i in 3:
#     if i+2 < len(dict_of_bushes):
#         harvest = dict_of_bushes[i] + dict_of_bushes[i+1] + dict_of_bushes[i+2]
#     if i+2 == len(dict_of_bushes):
#         harvest = dict_of_bushes[i] + dict_of_bushes[i+1] + dict_of_bushes[0]
#     else:
#         harvest = dict_of_bushes[i] + dict_of_bushes[i-3] + dict_of_bushes[i-2]
#     if harvest > max_harvest:
#         max_harvest = harvest

# print(max_harvest)

# n = int(input('Введите число кустов: '))
# a = list(map(int, input(
#     f"Введите количество ягод на кустах в строку через пробел: ").split()))

# max_sum = 0
# for i in range(n):
#     if i == 0:
#         curr_sum = a[i] + a[i + 1] + a[n - 1]
#     elif i == n - 1:
#         curr_sum = a[i] + a[i - 1] + a[0]
#     else:
#         curr_sum = a[i] + a[i - 1] + a[i + 1]
#     if curr_sum > max_sum:
#         max_sum = curr_sum

# print(max_sum)

# Эталонное решение
n = int(input())
arr = list()
for i in range(n):
    x = int(input())
    arr.append(x)
arr_count = list()
for i in range(len(arr) - 1):
    arr_count.append(arr[i - 1] + arr[i] + arr[i + 1])
arr_count.append(arr[-2] + arr[-1] + arr[0])
print(max(arr_count))
