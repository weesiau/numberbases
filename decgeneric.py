def decimal_gen(dec):
    num = int(dec)
    base = int(input("Enter the number base(2,8,16): "))
    result = []
    while (num > 0):
        rem = num % base
        result.append(str(rem))
        num = num // base
    result.reverse()
    return(''.join(result))


# main
print(decimal_gen(95))
