import sys
import time
from collections import deque

# 주석------------
sys.stdin = open('/Users/home/Developer/study/Algorithm/python/python.txt', 'r')
start = time.time()
input = sys.stdin.readline
#----------------

N = int(input())
A = [list(map(int, input().split()) ) for _ in range(N)]
a = A

for i in range(1, N):
    a[i][0] = min(A[i-1][1], A[i-1][2]) + A[i][0]
    a[i][1] = min(A[i-1][0], A[i-1][2]) + A[i][1]
    a[i][2] = min(A[i-1][0], A[i-1][1]) + A[i][2]

print(min(a[N - 1]))    

# 주석------------
print(f"time : {time.time() - start:.5f} sec")
# ---------------
