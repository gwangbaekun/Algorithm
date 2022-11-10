import sys
import time
# 주석------------
# sys.stdin = open('python.txt', 'r')
# start = time.time()
#----------------

N = int(sys.stdin.readline())

for _ in range(N):
    number_of_clothes = int(sys.stdin.readline())
    clothes = {}
    for _ in range(number_of_clothes):
        input = (sys.stdin.readline().split(" "))
        if (input[1].strip() in clothes):
            clothes[input[1].strip()] += 1
        else:
            clothes[input[1].strip()] = 1
    count = 1
    for i in clothes.values():
        count *= i + 1
    print(count - 1)

# 주석------------
# print("time : ", time.time() - start)
# ----------------