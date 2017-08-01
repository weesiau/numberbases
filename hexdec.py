bases = {'1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8',\
         '9':'9','A':'10','B':'11','C':'12','D':'13','E':'14','F':'15'}

def hexa_decimal():
    num = str(input("Enter hexadecimal number: "))
    hexa = list(num)
    hexa.reverse()
    dec = 0
    base = 16
    for i in range(0,len(hexa)):
        num = int(bases[hexa[i]])*(base**i)
        dec += num
    return dec

# main
print(hexa_decimal())

