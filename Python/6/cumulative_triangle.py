def cumulative_triangle(n):
    i = 1
    k = 1
    while k<=n:
        if n==k:
            return (i+i+k-1)*(i+k-1-i+1)//2
        i += k
        k += 1


if __name__ == '__main__':
    print(cumulative_triangle(5))
    # result: 65
