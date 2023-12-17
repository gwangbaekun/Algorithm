import sys
import time
from collections import deque

# 주석------------
sys.stdin = open('/Users/home/Developer/study/Algorithm/python/python.txt', 'r')
start = time.time()
#----------------

q = deque()
N = int(sys.stdin.readline())

for _ in range(N):
    cmd = list(map(int, sys.stdin.readline().split()))
    if cmd[0] == 1:
        q.appendleft(cmd[1])
    elif cmd[0] == 2:
        q.append(cmd[1])
    elif cmd[0] == 3:
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif cmd[0] == 4:
        if q:
            print(q.pop())
        else:
            print(-1)
    elif cmd[0] == 5:
        print(len(q))
    elif cmd[0] == 6:
        if q:
            print(0)
        else:
            print(1)
    elif cmd[0] == 7:
        if q:
            print(q[0])
        else:
            print(-1)
    elif cmd[0] == 8:
        if q:
            print(q[-1])
        else:
            print(-1)

# 주석------------
print(f"time : {time.time() - start:.5f} sec")
# ---------------
