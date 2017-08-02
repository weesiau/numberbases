def decimal_binary(dec):
    num = int(dec)
    binary = []
    while (num > 0):
        rem = num % 2
        binary.append(str(rem))
        num = num // 2
    binary.reverse()
    return(''.join(binary))

def magicnumber(low,high):
    numbers = []
    box1 = []
    for i in range(low,high+1):
        numbers.append(list((decimal_binary(i))))
        if int((numbers[i-1])[-1]) == 1:
            box1.append((numbers[i-1])[-1])
    print(box1)



# main
print(magicnumber(1,31))
