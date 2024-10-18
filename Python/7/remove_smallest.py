def remove_smallest(numbers: list):
    if len(numbers) == 0:
        return []
    else:
        num = numbers.copy()
        m = numbers[0]
        for i in range(len(num)):
            if m > num[i]:
                m = num[i]
    num.remove(m)
    return num


print(remove_smallest([2, 2, 1, 2, 1]))  # result: [2, 2, 2, 1]
