def encrypt_this(text):
    text = text.split()
    satr = ""
    for i in text:
        if len(i) == 1:
            satr += f"{ord(i[0])} "
        elif len(i) == 2:
            satr += f"{ord(i[0])}{i[1]} "
        elif len(i) > 2:
            satr += f"{ord(i[0])}{i[-1]}{i[2:len(i) - 1]}{i[1]} "
    return satr[0:len(satr) - 1]


print(encrypt_this('Hello'))  # result: 72olle
