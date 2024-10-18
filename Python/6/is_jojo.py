regex = ''


def is_jojo(name:str):
    name = name.lower().split()
    if len(name)<2:
        return False
    return name[0].startswith("jo") and name[1].startswith("jo") or name[0].startswith("jo") and name[1].endswith("jo") or name[0].startswith("gio") and name[1].startswith("gio")


# print(is_jojo('Joseph Joestar'))  # result: True
