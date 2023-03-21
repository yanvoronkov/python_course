# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

# text = input().split()
# text_new = ''
# for i in range(len(text)):
#     if text[:i].count(text[i]) > 0:
#         text_new += text[i] + '_' + str(text[:i].count(text[i])) + ' '
#     else:
#         text_new += text[i] + ' '
# print(text_new)

s = ("a a a b c a a d c d d").split()
dict = {}
for i in s:
    if i not in dict:
        dict[i] = 0
        print(i, end=' ')
    elif i in dict:
        dict[i] += 1
        print(f'{i}_{dict[i]}', end=' ')
