def dig_pow(n, p):
    charNum = str(n)
    output = 0
    for charIndex in range(0,len(charNum)):
        char = int(charNum[charIndex])
        output += char ** (p + charIndex)
    count = 0
    if (int(output / n) == output / n):
        return output / n
    else:
        return -1