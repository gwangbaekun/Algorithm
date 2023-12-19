import sys
import time
from collections import deque

# 주석------------
sys.stdin = open('/Users/home/Developer/study/Algorithm/python/python.txt', 'r')
start = time.time()
#----------------

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
C = list(map(int, sys.stdin.readline().split()))

queue = deque()
for i in range(N):
    if A[i] == 0:
        queue.appendleft(B[i])

for i in range(M):
    queue.append(C[i])
    print(queue.popleft(), end=" ")

# 주석------------
print(f"time : {time.time() - start:.5f} sec")
# ---------------
