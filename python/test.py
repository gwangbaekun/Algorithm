import time
import sys

# 주석------------
# sys.stdin = open('python.txt', 'r')
# start = time.time()
#----------------

N = int(sys.stdin.readline())

check_list = [0] * 10001

nums = []
for i in range(N):
    num = int(sys.stdin.readline().strip())

    check_list[num] = check_list[num] + 1

for i in range(10001):
    if check_list[i] != 0:
        for j in range(check_list[i]):
            print(i) 
# 주석------------
# print("time : ", time.time() - start)
#----------------
