def narcissistic( value ):
    charVal = str(value)
    charLen = len(charVal)
    narcissisticNum = 0
    for char in charVal:
        narcissisticNum += int(char) ** charLen
    if (int(narcissisticNum) == value):
        return True
    else:
        return False
    