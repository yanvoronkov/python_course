# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k
# ), не превосходящие числа N.

n = int(input('Введите сисло N: '))
i = 0
print(f"{n} -> ", end='')
while n > 2 ** i:
    print(2 ** i, end=' ')
    i += 1
