from collections import Counter

def custom_sort(chars: list):
    return sorted(
        chars, key=lambda c: (
            c.isdigit(), 
            c.isalpha(), 
            c
        )
    )

def find_characters(matrix: str):
    counter = Counter(matrix.replace('\n', ''))

    min_count = min(counter.values())
    min_chars = [
        char for char, count in counter.items() \
        if count == min_count
    ]
    if len(min_chars) == 1:
        return str(min_chars[0])
    return ''.join(custom_sort(min_chars))


if __name__ == "__main__":
    test = '''\
        3v652
        1uwyt
        v254v
        t54tv
        x45yx
        s7x45
        5402v
        2x3xw
        5w22v\
    '''
    print(find_characters(test))