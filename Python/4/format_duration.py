"""https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python"""

def format_duration(seconds):
    if seconds == 0:
        return "now"

    time_units = {
        "year": 365 * 24 * 3600,
        "day": 24 * 3600,
        "hour": 3600,
        "minute": 60,
        "second": 1
    }

    time_parts = []

    for unit, unit_seconds in time_units.items():
        if seconds >= unit_seconds:
            value = seconds // unit_seconds
            seconds %= unit_seconds
            time_parts.append(
                f"{value} {unit}{'s' if value > 1 else ''}"
            )

    if len(time_parts) > 1:
        return ', '.join(time_parts[:-1]) \
            + ' and ' + time_parts[-1]
    
    return time_parts[0]

if __name__ == '__main__':
    print(format_duration(205851834))
