def what_time_is_it(angle1):
    angle = angle1//30
    hh = f"{12 if 0 == angle else int(angle) if angle > 9 else f'0{int(angle)}'}:"
    angle = (angle1-angle*30)*2
    mm = f"{'00' if 0 == angle else int(angle) if angle >= 10 else f'0{int(angle)}'}"
    return f"{hh}{mm}"


print(what_time_is_it(360))  # result: 12:00
