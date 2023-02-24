import sys
import time
from collections import deque

# 주석------------
# sys.stdin = open('python.txt', 'r')
# start = time.time()
#----------------

N = int(sys.stdin.readline())
k = int(sys.stdin.readline())

start = 1
end = k
answer = 0

while start <= end:
    mid = (start + end) // 2
    count = 0

    for i in range(1, N+1):
        count += min(mid // i, N)

    if count >= k:
        end = mid - 1
        answer = mid
    else:
        start = mid + 1

print(answer)

# 주석------------
# print(f"time : {time.time() - start:.5f} sec")
# ---------------