import math
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





print(dashatize(-790266962712808847))