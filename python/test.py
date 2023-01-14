import sys
import time
import copy

# 주석------------
sys.stdin = open('python.txt', 'r')
start = time.time()
#----------------

N = int(sys.stdin.readline())

dp = [0] * 1000001
dp[1] = 1
dp[2] = 2

for k in range(3, N+1):
    dp[k] = (dp[k-1] + dp[k-2]) % 15746

print(dp[N])

# 주석------------
print("time : ", time.time() - start)
# ---------------