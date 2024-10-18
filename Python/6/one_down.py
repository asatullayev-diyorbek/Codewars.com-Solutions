def one_down(txt):
    if type(txt) is not str:
        return "Input is not a string"
    if txt == "":
        return ""
    if not txt:
        return ""

    satr = ""
    for i in txt:
        if i.isalpha():
            if i == "A" or i == "a":
                satr += "Z" if i.isupper() else "z"
            else:
                satr += chr((ord(i) - 1))
        else:
            satr += i
    return satr


print(one_down('Ifmmp'))  # result: Hello
