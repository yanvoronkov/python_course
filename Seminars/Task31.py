# Задача №31. Решение в группах
# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ...,
# где a0= 0, a1 = 1, ak
#  = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию

def fibonachy(num):
    if num == 1 or num == 0:
        return 1
    return fibonachy(num-1) + fibonachy(num-2)


number = int(input("Введите число: "))
print(fibonachy(number))
