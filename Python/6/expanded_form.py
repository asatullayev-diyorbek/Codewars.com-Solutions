def expanded_form(num: int):
    nums = [int(i) for i in str(num)]
    length = len(nums)

    result = [str(n * 10 ** (length - idx - 1)) \
              for idx, n in enumerate(nums) \
                   if n != 0]

    return ' + '.join(result)


if __name__ == '__main__':
    print(expanded_form(70304))
