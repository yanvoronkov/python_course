# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

number_coins = int(input('Введите количество монет: '))
number_coins_side1 = 0
number_coins_side2 = 0
for i in range(1, number_coins+1):
    side_coin = int(input('Введите сторону монеты (1 или 2): '))
    if side_coin == 1:
        number_coins_side1 += 1
    else:
        number_coins_side2 += 1
if number_coins_side1 <= number_coins_side2:
    print(f"{number_coins} -> нужно перевернуть {number_coins_side1} монет")
else:
    print(f"{number_coins} -> нужно перевернуть {number_coins_side2} монет")
