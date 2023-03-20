# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строк

list_numbers = int(input('Введите число элементов списка: '))
list_1 = []

for i in range(list_numbers):
    list_1.append(int(input(f"Введите значение {i+1} списка: ")))
number_x = int(input('Введите заданное число X: '))

min_val = int(abs(list_1[0] - number_x))
min_num = list_1[0]
for i in list_1:
    if (abs(i - number_x)) < min_val:
        min_num = i
print(list_numbers)
print(list_1)
print(number_x)
print(min_num)
