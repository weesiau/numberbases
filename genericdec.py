bases = {'1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8',\
         '9':'9','A':'10','B':'11','C':'12','D':'13','E':'14','F':'15'}

def gen_decimal():
    num = str(input("Enter number: "))
    base = int(input("Enter base to be converted from(2,8,16): "))
    listnum = list(num)
    listnum.reverse()
    dec = 0
    for i in range(0,len(listnum)):
        num = int(bases[listnum[i]])*(base**i)
        dec += num
    return dec

# main
print(gen_decimal())

