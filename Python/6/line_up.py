def line_up(cmd):
    """
        1-oldi,2-o'ng,3-orqa,4-chap
    """

    jinniroq = 1
    soglom = 1
    soni = 0
    for i in cmd:
        if i == "L":
            jinniroq = 4 if jinniroq == 1 else jinniroq-1
            soglom = 1 if soglom == 4 else soglom+1
        elif i == "R":
            jinniroq = 1 if jinniroq == 4 else jinniroq + 1
            soglom = 4 if soglom == 1 else soglom - 1
        elif i == "A":
            jinniroq = (jinniroq + 2) % 4 if (jinniroq+2) % 4 != 0 else 4
            soglom = (soglom + 2) % 4 if (soglom+2) % 4 != 0 else 4

        if jinniroq == soglom:
            soni += 1
    return soni


print(line_up('RRRRRRRRRRLLLLLLLLLRRRRLLLLLLLLLL'))  # result: 16
