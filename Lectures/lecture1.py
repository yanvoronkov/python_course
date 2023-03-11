
n = 5
v = "Привет"

# print(type(n))

# print(f"{n} - {v}")
# print("{} - {}".format(1,"Ghbdt"))

# print('Введите первую строку: ')
# a = input()
# print(a)
# b = input('Введите 2 число: ')
# print(a, '+', b, '=', a+b)

# c = 5.89
# print(c)
# print(type(c))
# n = int(c)
# print(n)
# print(type(n))


# print('Введите первую строку: ')
# a = int(input())
# b = int(input('Введите 2 число: '))
# print(a, '+', b, '=', a+b)

# Округление чисел
# a = 5.8967
# b = 6.4445
# print(round(a*b, 3))

# iter = 2
# iter += 3  # iter = iter + 3
# iter -= 4  # iter = iter - 4


# a = 1 > 4
# print(a)

# a = 1 < 4 and 5 > 2
# print(a)

# a = 1 == 2
# print(a)

# a = 1 != 2
# print(a)

# a = 'dssds'
# b = 'dssds'
# print(a == b)

# a = 1 < 3 < 2 < 10
# print(a)


# userName = input('Введите имя: ')

# if userName == 'Маша':
#     print('Ура, это же Маша!')
# elif userName == 'Марина':
#     print('Привет, Мариша!!')
# elif userName == 'Ильнар':
#     print('Привет, Ильнар!')
# else:
#     print('Привет,', userName)

# i = 0
# while i < 5:
#     if i == 3:
#         break
#     i = i + 1
# else:
#     print('Пожалуй')
#     print('Хватит )')
# print(i) #выводися 3, так как принудительно остановлен цикл

# i = 0
# while i < 5:
#     i = i + 1
# else:
#     print('Пожалуй')
#     print('Хватит )')
# print(i)  # выводися текст из блока после else и 5, так как цикл сам заершился

# n = int(input())
# flag = True
# i = 2
# while flag:
#     if n % i == 0:
#         flag = False
#         print(i)
#     elif i > n // 2:
#         print(n)
#         flag = False
#     i += 1

# a = 'qwerty'
# print(a[2])

# a = 'qwerty'
# for i in a:
#     print(i)


# line = ""
# for i in range(5):
#     line = ""
#     for i in range(5):
#         line += "*"
#     print(line)

text = 'СъЕШь Еще ЭТих мягких БулоЧЕК'
print(len(text))
print('eще' in text)
print(text.lower())
print(text.upper())
print(text.replace('Еще', 'еще'))
print(text[0])
print(text[-1])
print(text[len(text)-1])
print(text[:])
print(text[:2])
print(text[4:])
print(text[2:9])
print(text[6:-12])
print(text[6:-12:2])  # добавили шаг
text = text[2:3] + text[2:3] + text[2:3]
print(text)
