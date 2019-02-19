def linearSearch(n):
    for i in range(len(lst)):
        if n == lst[i - 1]:
            return i

    return -1

lst = [8, 5, 3, 7, 1, 9, 2, 6]
print(linearSearch(4))
