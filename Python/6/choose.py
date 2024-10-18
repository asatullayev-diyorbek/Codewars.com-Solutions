def choose(n, k):
    if n < k:
        return 0
    else:
        f1 = 1
        f2 = 1
        f3 = 1
        for i in range(1, n+1):
            f1 *= i
            if i <= k:
                f2 *= i
            if i <= n-k:
                f3 *= i
    return f1 // (f2 * f3)


print(choose(1, 1))  # result: 1
