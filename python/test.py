import sys
import time
import operator
from collections import deque

# 주석------------
sys.stdin = open('/Users/home/Developer/study/Algorithm/python/python.txt', 'r')
start = time.time()
#----------------

a0, a1 = map(int, sys.stdin.readline().split(" "))
c = int(sys.stdin.readline())
n0 = int(sys.stdin.readline())

if (a1 * n0 + a0 <= c * n0) and a1 <= c:
    print(1)
else:
    print(0)

# 주석------------
print(f"time : {time.time() - start:.5f} sec")
# ---------------

