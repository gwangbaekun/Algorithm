import sys
import time

# 주석------------
sys.stdin = open('python.txt', 'r')
start = time.time()
#----------------

A, B = map(int, sys.stdin.readline().split(" "))
arr = list(map(int, sys.stdin.readline().split(" ")))
prefixsum = []
total = 0
for i in range(len(arr)):
    total += arr[i]
    prefixsum.append(total)

for _ in range(B):
    N, M = map(int, sys.stdin.readline().split(" "))
    if N == 1:
        print(prefixsum[M - 1])
    else:
        print(prefixsum[M - 1] - prefixsum[N - 2])

# 주석------------
print(f"time : {time.time() - start:.5f} sec")
# ---------------