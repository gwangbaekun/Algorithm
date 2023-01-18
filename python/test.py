import sys
import time
import copy

# 주석------------
# sys.stdin = open('python.txt', 'r')
# start = time.time()
#----------------

# setup
N = int(sys.stdin.readline())
triangle = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]

for i in range(1, N):
    for j in range(i + 1):
        if j == 0:
            triangle[i][j] = triangle[i-1][j] + triangle[i][j]
        elif j == i:
            triangle[i][j] = triangle[i-1][j-1] + triangle[i][j]
        else:
            triangle[i][j] = max(triangle[i-1][j], triangle[i-1][j-1]) + triangle[i][j]

print(max(triangle[N-1]))
# 주석------------
# print(f"time : {time.time() - start:.5f} sec")
# ---------------