# def f(x):
#     return x*x


# a = f

# print(a(5))
# print(f(5))


# def calc_1(a, b):
#     return a + b


# def calc_2(a, b):
#     return a * b


# def math(op, x, y):
#     print(op(x, y))


# math(calc_1, 5, 5)

# def calc_2(a, b):
#     return a * b


# def math(op, x, y):
#     print(op(x, y))


# def calc_1(a, b): return a + b


# math(calc_1, 5, 5)

list_1 = [1, 2, 3, 5, 8, 15, 23, 38]


def num_and_square(list):
    list_2 = []
    for i in list:
        if i % 2 == 0:
            list_2.append((i, i*i))
    return list_2


result = num_and_square(list_1)
print(result)
