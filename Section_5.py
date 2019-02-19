def listInsert(n):
    if not lst:
        lst.append(n)
        return True
    i = 0
    while i < len(lst):
        if n <= lst[i]:
            lst.insert(i, n)
            return True
        i += 1
        
    if n >= lst[len(lst) - 1]:
        lst.append(n)
        return True

lst = [2,3,3,5,6,7,9,10]
print(listInsert(6))
print(lst)
