import sys
import time
from collections import deque

# 주석------------
sys.stdin = open('/Users/home/Developer/study/Algorithm/python/python.txt', 'r')
start = time.time()
#----------------

N = int(sys.stdin.readline())
answer = 1

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(N))

# 주석------------
print(f"time : {time.time() - start:.5f} sec")
# ---------------
