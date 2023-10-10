import sys
import time

# 주석------------
# sys.stdin = open('/Users/home/Developer/study/Algorithm/python/python.txt', 'r')
# start = time.time()
#----------------

N, M = map(int, sys.stdin.readline().split())

A = []
B = []

for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().split(" "))))

for i in range(N):
    B.append(list(map(int, sys.stdin.readline().split(" "))))

for i in range(N):
    for j in range(M):
        A[i][j] += B[i][j]

for i in range(N):
    print(*A[i])

# 주석------------
# print(f"time : {time.time() - start:.5f} sec")
# ---------------

