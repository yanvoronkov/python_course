# Задача 8: Требуется определить, можно ли от шоколадки
# размером n × m долек отломить k долек, если разрешается
# сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input('Введите размер n шоколадки: '))
m = int(input('Введите размер m шоколадки: '))
k = int(input('Введите число долек: '))

if (k < n * m) and (k % m == 0 or k % n == 0):
    print(f"{n} {m} {k} -> yes")
else:
    print(f"{n} {m} {k} -> no")
