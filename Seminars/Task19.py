# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

list_1 = [1, 2, 3, 4, 5]
k = 3 % len(list_1)
print(list_1[k:] + list_1[:k])

# Вариант 2:
# list_1 = [1, 2, 3, 4, 5]
# k = 6 % len(list_1)

# for i in range(k):
#     num = list_1.pop(-1)
#     list_1.insert(0, num)
# print(list_1)
