import sys

# sys.stdin = open("python.txt", "r")
N = int(sys.stdin.readline())

# 분자: 1 / 1, 2 / 3, 2, 1 / 1, 2, 3, 4
# 분모: 1 / 2, 1 / 1, 2, 3 / 4, 3, 2, 1

roomNum = 0
rooms = 0
while N > rooms:
    roomNum += 1
    rooms += roomNum
    if roomNum % 2 == 1:
        top = rooms + 1 - N
        bottom = roomNum + 1 - top
    else:
        bottom = rooms + 1 - N
        top = roomNum + 1 - bottom


print(str(top) + "/" + str(bottom))

