import sys
import time
from collections import deque

# 주석------------
sys.stdin = open('/Users/home/Developer/study/Algorithm/python/python.txt', 'r')
start = time.time()
#----------------

q = deque()
l = []
N, K = map(int, sys.stdin.readline().split())

for i in range(N):
    q.append(i + 1)

while len(l) != N:
    for i in range(K - 1):
        q.append(q.popleft())
    l.append(q.popleft())

print('<' + ', '.join(str(x) for x in l) + '>')

# 주석------------
print(f"time : {time.time() - start:.5f} sec")
# ---------------
