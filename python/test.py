import sys
import time
from collections import deque

# 주석------------
sys.stdin = open('/Users/home/Developer/study/Algorithm/python/python.txt', 'r')
start = time.time()
#----------------

def recv(n, start, end):
    if n == 1:
        print(start, end)
        return
    
    recv(n - 1, start, 6 - start - end)
    print(start, end)
    recv(n - 1, 6 - start - end, end)


N = int(sys.stdin.readline())
print(2 ** N - 1)
recv(N, 1, 3)

# 주석------------
print(f"time : {time.time() - start:.5f} sec")
# ---------------
