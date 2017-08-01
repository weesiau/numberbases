def octal_decimal(num):
    octal = list(str(num))
    octal.reverse()
    dec = 0
    base = 8
    for i in range(0,len(octal)):
        num = int(octal[i])*(base**i)
        dec += num
    return dec

# main
print(octal_decimal(63))

