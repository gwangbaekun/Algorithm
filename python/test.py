import time
import sys

# 주석------------
# sys.stdin = open('python.txt', 'r')
# start = time.time()
#----------------

N = int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in arr:
    i.reverse()

arr.sort()

for i in arr:
    i.reverse()
    print(i[0], i[1])

# 주석------------
# print("time : ", time.time() - start)
#----------------