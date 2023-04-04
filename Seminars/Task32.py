# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)


def find_items_in_range(list, min, max):
    result_list = []
    for i in range(len(list)):
        if min <= list[i] <= max:
            result_list.append(i)
    return result_list


input_list = [2, 4, 23, 45, 12, 8, 3, 2, 1, 45, 67]
min = 3
max = 40
result_list = find_items_in_range(input_list, min, max)
print(result_list)
