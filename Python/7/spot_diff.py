def spot_diff(s1, s2):
    diff = []
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            diff.append(i)
    return diff


print(spot_diff('Hello World!', 'hello world.'))  # [0, 6, 11]
