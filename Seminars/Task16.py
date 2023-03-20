# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X
# в списке A[1..N]. Пользователь в первой строке вводит натуральное число N
# – количество элементов в списке. В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

list_numbers = int(input('Введите число элементов списка: '))
list_1 = []
count = 0
for i in range(list_numbers):
    list_1.append(int(input(f"Введите значение {i+1} списка: ")))
find_number = int(input('Введите искомое значение: '))
for i in list_1:
    if i == find_number:
        count += 1
print(list_numbers)
print(list_1)
print(find_number)
print(count)
