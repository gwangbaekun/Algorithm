import sys
import time
from collections import deque

# 주석------------
sys.stdin = open('/Users/home/Developer/study/Algorithm/python/python.txt', 'r')
start = time.time()
#----------------

N = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))

q = deque([i for i in range(1, N + 1)])
i = 0

for _ in range(N):
    pl = q.popleft()
    print(pl, end=' ')
    if l[pl - 1] > 0:
        i = l[pl - 1] - 1
    else:
        i = l[pl - 1]
    q.rotate(-i)

# 주석------------
print(f"time : {time.time() - start:.5f} sec")
# ---------------
