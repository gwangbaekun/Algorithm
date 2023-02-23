import sys
import time
from collections import deque

# 주석------------
# sys.stdin = open('python.txt', 'r')
# start = time.time()
#----------------

N, C = map(int, sys.stdin.readline().split(" "))
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))

arr.sort()
start = 1
end = arr[N - 1] - arr[0]
answer = 0

while start <= end:
    mid = (start + end) // 2
    cur = arr[0]
    count = 1

    for i in range(1, N):
        if arr[i] >= cur + mid:
            count += 1
            cur = arr[i]
    
    if count >= C:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)

# 주석------------
# print(f"time : {time.time() - start:.5f} sec")
# ---------------