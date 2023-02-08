import sys
import time

# 주석------------
# sys.stdin = open('python.txt', 'r')
# start = time.time()
#----------------

N, K = map(int, sys.stdin.readline().split(" "))
arr = [int(sys.stdin.readline()) for _ in range(N)]


start, end = 1, max(arr)
count = 0

while 2 ** count < max(arr):
    count += 1

for i in range(count):
    mid = (start + end) // 2
    c = 0
    for elem in arr:
        c += elem // mid
    
    if c >= K:
        start = mid + 1
    else:
        end = mid - 1

print(end)

# 주석------------
# print(f"time : {time.time() - start:.5f} sec")
# ---------------