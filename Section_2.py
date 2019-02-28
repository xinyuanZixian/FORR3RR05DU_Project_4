def linearSearch(n):
    for i in range(len(lst)):
        if n == lst[i]:
            return i + 1

    return -1

lst = [8, 5, 3, 7, 1, 9, 2, 6]
print(linearSearch(6))
