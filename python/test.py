import sys
import time

# 주석------------
sys.stdin = open('python.txt', 'r')
start = time.time()
#----------------

N, K = map(int, sys.stdin.readline().split(" "))
arr = list(map(int, sys.stdin.readline().split(" ")))

start, end = max(arr) - K, max(arr)

while start <= end:
    mid = (start + end) // 2
    lo = 0
    for elem in arr:
        if elem > mid:
            lo += elem - mid

    if lo >= K:
        start = mid + 1
    else:
        end = mid - 1

print(end)

# 주석------------
print(f"time : {time.time() - start:.5f} sec")
# ---------------