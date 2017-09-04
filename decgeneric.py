hexabases = {'1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7',\
             '8':'8','9':'9','10':'A','11':'B','12':'C','13':'D','14':'E',\
             '15':'F'}

def decgen(dec):
    num = int(dec)
    base = int(input("Enter the base you want to convert to."))
    if base != 2 or 8 or 16:
        print("cannot convert hehexd")
    result = []
    while num > 0:
        rem = num % base
        if base == 16:
            result.append(hexabases[str(rem)])
        else:
            result.append(str(rem))
        num = num // base
    result.reverse()
    return(''.join(result))


print(decgen(95))

