def binarySearch(n):
    return binarySearchRecursion(n, lst, 0, len(lst) - 1)

def binarySearchRecursion(n, lst, start, end):
    if start > end:
        return -1
    mid = start + (end - start) // 2
    if lst[mid] > n:
        return binarySearchRecursion(n, lst, start, mid - 1)
    if lst[mid] < n:
        return binarySearchRecursion(n, lst, mid + 1, end)
    return mid + 1

lst = [1, 2, 3, 5, 6, 7, 8, 9]
print(binarySearch(11))
