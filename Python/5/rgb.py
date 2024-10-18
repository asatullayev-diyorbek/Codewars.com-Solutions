def rgb(r, g, b):
    if 0 < r:
        r = r if 255 >= r else 255
        r16 = (str(r // 16 if 9 >= r // 16 else (chr(65 + r // 16 - 10))) +
               str(r % 16 if r % 16 <= 9 else (chr(65 + r % 16 - 10))))
    else:
        r16 = "00"
    if 0 < g:
        g = 255 if g > 255 else g
        g16 = (str(g // 16 if g // 16 <= 9 else (chr(65 + g // 16 - 10))) +
               str(g % 16 if g % 16 <= 9 else (chr(65 + g % 16 - 10))))
    else:
        g16 = "00"
    if b > 0:
        b = b if b <= 255 else 255
        b16 = str(b // 16 if b // 16 <= 9 else (chr(65 + b // 16 - 10))) + str(
            b % 16 if b % 16 <= 9 else (chr(65 + b % 16 - 10)))
    else:
        b16 = "00"
    return f"{r16}{g16}{b16}"


print(rgb(255, 255, 255))  # result: FFFFFF
