import sys
import time
from collections import deque

# 주석------------
sys.stdin = open('/Users/home/Developer/study/Algorithm/python/python.txt', 'r')
start = time.time()
#----------------

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split(" ")))

dp = [1 for i in range(N)]

for i in range(N):
     for j in range(i):
          if A[i] > A[j]:
               dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

# 주석------------
print(f"time : {time.time() - start:.5f} sec")
# ---------------

