my_list = [1, 2, 5, 6, 7, 8, 9]


def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = round((low + high)/2)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


print(binary_search(my_list, 6))
