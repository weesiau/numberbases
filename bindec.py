def binary_decimal(num):
    b = list(str(num))
    b.reverse()
    dec = 0
    base = 2
    for i in range(0,len(b)):
        num = int(b[i])*(base**i)
        dec += num
    return dec

# main
print(binary_decimal(10110))
