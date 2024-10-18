import math


def polybius(st):
    satr = ""
    for i in st.upper():
        if i.isalpha():
            if i == "I" or i == "J":
                satr += "24"
            else:
                satr += "{0}{1}".format(str(math.ceil((ord(i) - 64 - ord(i) // 75) / 5)), (
                    str(math.ceil((ord(i) - 64 - ord(i) // 75) % 5)) if math.ceil(
                        (ord(i) - 64 - ord(i) // 75) % 5) != 0 else "5"))
        else:
            satr += i
    return satr


print(polybius('POLYBIUS'))  # result: 3534315412244543
