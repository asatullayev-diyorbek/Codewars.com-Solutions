"""https://www.codewars.com/kata/513e08acc600c94f01000001/python"""

def to_hex(n):
    n = max(0, min(255, n))
    return f"{n:02X}"

def rgb(r, g, b):
    return f"{to_hex(r)}{to_hex(g)}{to_hex(b)}"


if __name__ == '__main__':
    print(rgb(255, 255, 255))
