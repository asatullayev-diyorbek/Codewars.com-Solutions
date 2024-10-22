"""https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/python"""


def snail(snail_map):
    expected = []
    if not snail_map:
        return expected

    r_min, r_max = 0, len(snail_map) - 1
    c_min, c_max = 0, len(snail_map[0]) - 1

    while r_min <= r_max and c_min <= c_max:
        expected.extend(
            list(
                snail_map[r_min][c]
                for c in range(c_min, c_max + 1)
            )
        )
        r_min += 1

        expected.extend(
            list(
                snail_map[r][c_max] 
                for r in range(r_min, r_max + 1)
            )
        )
        c_max -= 1

        if r_min <= r_max:
            expected.extend(
                list(
                    snail_map[r_max][c] 
                    for c in range(c_max, c_min - 1, -1)
                )
            )
            r_max -= 1

        if c_min <= c_max:
            expected.extend(
                list(
                    snail_map[r][c_min] 
                    for r in range(r_max, r_min - 1, -1)
                )
            )
            c_min += 1

    return expected


# Testlar
if __name__ == '__main__':
    test1 = [
        [1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ]
    test2 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print(snail(test1))  # [1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 16, 11, 6, 7, 8, 9, 14, 19, 18, 17, 12, 13]
    print(snail(test2))  # [1, 2, 3, 6, 9, 8, 7, 4, 5]

