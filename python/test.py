import sys
import time

# 주석------------
sys.stdin = open('/Users/jeyeolbaek/Developer/study/Algorithm/python/python.txt', 'r')
start = time.time()
#----------------
input = sys.stdin.readline
#----------------

N = int(input())
arr = list(int(input()) for _ in range(N))
dp = [[0,0,0] for _ in range(N)]

dp[0] = [arr[0], 0, 0]

for i in range(1, N):
    dp[i][0] = dp[i-1][2] + arr[i]
    dp[i][1] = dp[i-1][0] + arr[i]
    dp[i][2] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2])

print(max(dp[-1]))

# 주석------------
print(f"time : {time.time() - start:.5f} sec")
# ---------------
