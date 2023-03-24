# Задача №33. Общее обсуждение
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

# Мой вариант:
# n = [1, 3, 3, 3, 4]

# def change(n):
#     max = n[0]
#     min = n[0]
#     m = n
#     for i in n:
#         if n[i] > max:
#             max = n[i]
#         if n[i] < min:
#             min = n[i]
#     for i in n:
#         if m[i] == max:
#             m[i] = min
#         else:
#             m[i] = n[i]
#     return m

# print(change(n))

# Вариант преподавателя:

def min_max_serch(input_list):
    return min(input_list), max(input_list)


def min_max_replace(start_list, copy=True):
    if copy:
        start_list = start_list.copy()
    min_el, max_el = min_max_serch(start_list)
    while max_el in start_list:
        max_index = start_list.index(max_el)
        start_list[max_index] = min_el
    return start_list


start_list = [1, 4, 3, 5, 4]
print(min_max_replace(start_list))
