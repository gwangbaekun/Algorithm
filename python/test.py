import sys
import time
from collections import deque

# 주석------------
sys.stdin = open('/Users/home/Developer/study/Algorithm/python/python.txt', 'r')
start = time.time()
#----------------

N = int(sys.stdin.readline())

q = deque()
for i in range(N):
    q.append(i + 1)

while len(q) > 1:
    q.popleft()
    q.append(q.popleft())

print(q[0])

# 주석------------
print(f"time : {time.time() - start:.5f} sec")
# ---------------
