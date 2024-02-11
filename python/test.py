import sys
import time

# 주석------------
# sys.stdin = open('/Users/jeyeolbaek/Developer/study/Algorithm/python/python.txt', 'r')
# start = time.time()
#----------------
input = sys.stdin.readline
#----------------

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [1] * N
arr.sort(key=lambda x: (x[0], x[1]))

for i in range(1, N):
    for j in range(0, i):
        if arr[j][1] < arr[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))

# 주석------------
# print(f"time : {time.time() - start:.5f} sec")
# ---------------