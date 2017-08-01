def decimal_binary(dec):
    num = int(dec)
    binary = []
    while (num > 0):
        rem = num % 2
        binary.append(str(rem))
        num = num // 2
    binary.reverse()
    return(''.join(binary))


# main
print(decimal_binary(95))
