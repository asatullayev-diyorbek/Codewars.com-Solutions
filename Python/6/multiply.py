import math


def multiply(n, l):
    return list(map(lambda x: round(x / math.pow(n, -1)), l))


print(multiply(2, [1, 2, 3]))
