import sys
import time
import copy

# 주석------------
# sys.stdin = open('python.txt', 'r')
# start = time.time()
#----------------

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

for i in range(1, len(arr)):
    arr[i] = max(arr[i], arr[i-1] + arr[i])

print(max(arr))

# 주석------------
# print("time : ", time.time() - start)
# ---------------