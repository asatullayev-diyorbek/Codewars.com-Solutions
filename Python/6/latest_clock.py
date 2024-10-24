from datetime import timedelta
from itertools import permutations

def mixed(ls: list):
    ms = {
        f"{x[0]}{x[1]}" \
        for x in permutations(ls, 2)
    }
    return list(ms)


def latest_clock(a, b, c, d):
    digits = [a, b, c, d]

    valid_times = []
    choices = mixed(digits)
    for h in choices:  
        inline = digits.copy()
        inline.remove(int(h[0]))
        inline.remove(int(h[1]))
        inline_choices = mixed(inline) 
        for m in inline_choices:
            hour = int(h)
            minute = int(m)
            if hour <= 23 and minute <= 59:
                valid_times.append(
                    timedelta(
                        hours=hour, 
                        minutes=minute
                    )
                )

    latest_time = max(valid_times)
    hours = latest_time.seconds // 3600
    minutes = (latest_time.seconds % 3600) // 60
    return f"{hours:02}:{minutes:02}"


if __name__ == '__main__':
    print(latest_clock(2, 4, 0, 0)) 
    # result: 20:40