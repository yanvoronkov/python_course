# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.

list_1 = ('A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R')
list_2 = ['D', 'G']
list_3 = ['B', 'C', 'M', 'P']
list_4 = ['F', 'H', 'V', 'W', 'Y']
list_5 = ['K']
list_6 = ['J', 'X']
list_7 = ['Q', 'Z']
list_8 = ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']
list_9 = ['Д', 'К', 'Л', 'М', 'П', 'У']
list_10 = ['Б', 'Г', 'Ё', 'Ь', 'Я']
list_11 = ['Й', 'Ы']
list_12 = ['Ж', 'З', 'Х', 'Ц', 'Ч']
list_13 = ['Ш', 'Э', 'Ю']
list_14 = ['Ф', 'Щ', 'Ъ']

word = input('Введите слово: ')
sum_value = 0
for i in range(len(word)):
    if word[i] in list_1:
        sum_value += 1
    if word[i] in list_2:
        sum_value += 2
    if word[i] in list_3:
        sum_value += 3
    if word[i] in list_4:
        sum_value += 4
    if word[i] in list_5:
        sum_value += 5
    if word[i] in list_6:
        sum_value += 8
    if word[i] in list_7:
        sum_value += 10
    if word[i] in list_8:
        sum_value += 1
    if word[i] in list_9:
        sum_value += 2
    if word[i] in list_10:
        sum_value += 3
    if word[i] in list_11:
        sum_value += 4
    if word[i] in list_12:
        sum_value += 5
    if word[i] in list_13:
        sum_value += 8
    if word[i] in list_14:
        sum_value += 10
print(sum_value)
