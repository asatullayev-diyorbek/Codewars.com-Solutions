def reduce_fraction(fraction):
    sayi1, sayi2 = fraction
    while sayi2:
        sayi1, sayi2 = sayi2, sayi1 % sayi2
    return fraction[0] // sayi1, fraction[1] // sayi1


# print(reduce_fraction([45, 120]))  # result: [3, 8]
