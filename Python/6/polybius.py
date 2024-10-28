def polybius(st):
    result = ""
    for char in st.upper():
        if char.isalpha():
            if char in "IJ":
                result += "24"
            else:
                val = ord(char) - 65
                if char > "J":
                    val -= 1
                row = val // 5 + 1
                col = val % 5 + 1
                result += f"{row}{col}"
        else:
            result += char
    return result


if __name__ == '__main__':
    print(polybius('POLYBIUS'))  # result: 3534315412244543
