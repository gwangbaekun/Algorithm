import sys
import time
# 주석------------
sys.stdin = open('python.txt', 'r')
start = time.time()
#----------------

N, K = map(int, input().split())

dp = []

for i in range(N+1):
    dp.append([1]*(i+1))

for i in range(2, N+1):
    for j in range(1, i):
        dp[i][j] = (dp[i-1][j-1] + dp[i-1][j])%10007

print(dp[N][K])


# 주석------------
print("time : ", time.time() - start)
# ----------------