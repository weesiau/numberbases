bases = {'1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8',\
         '9':'9','10':'A','11':'B','12':'C','13':'D','14':'E','15':'F'}

def decimal_hexa(dec):
    num = int(dec)
    hexa = []
    while (num > 0):
        rem = num % 16
        hexa.append(bases[str(rem)])
        num = num // 16
    hexa.reverse()
    return(''.join(hexa))


# main
print(decimal_hexa(95))
