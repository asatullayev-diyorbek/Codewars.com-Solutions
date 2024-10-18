def remove_smallest(n, arr):
    if n < 0:
        return arr
    elif n >= len(arr):
        return []
    else:
        arr1 = arr.copy()
        for i in range(n):
            arr1.remove(min(arr1))
        return arr1


print(remove_smallest(2, [5, 3, 2, 1, 4]))  # result: [5, 3, 4]
