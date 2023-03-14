# По данному целому неотрицательному n вычислите значение n!.
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1
# Решить задачу используя цикл while

n = int(input('Введите число n: '))

factorial = 1
i = 2
while i <= n:
    factorial = factorial * i
    i += 1
print(factorial)
