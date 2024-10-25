def dashatize(n):
    n = str(n)
    n = n.strip('-')
    response = ''
    for i in n:
        if int(i) % 2 == 1:
            response += '-' + i + '-'
        else:
            response += i
    response = response.strip('-')
    response = response.replace('--', '-')
    return response


if __name__ == '__main__':
    print(dashatize(-790266962712808847))
    # result: 7-9-0266-9-62-7-1-280884-7
