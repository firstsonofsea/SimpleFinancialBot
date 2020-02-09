def com1(str1, str2, info):
    f = 0
    if str(str1).lower() in info:
        f = 1
    if f:
        for i in info:
            if i == str(str1).lower():
                info[i] += int(str2)
    else:
        info[str(str1).lower()] = int(str2)

def clean(info):
    global DATA
    DATA = {}

def com2(info):
    s = ''
    for i in info:
        s += i
        s += "    "
        s += str(info[i])
        s += "\n"
    return s
