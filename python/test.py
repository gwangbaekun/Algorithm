import sys
import time

# 주석------------
# sys.stdin = open("/Users/jeyeolbaek/Developer/study/Algorithm/python/python.txt", "r")
# start = time.time()
# ----------------
input = sys.stdin.readline
# ----------------


def min_merge_cost_dp(K, files):
    prefix_sum = [0] * (K + 1)
    for i in range(K):
        prefix_sum[i + 1] = prefix_sum[i] + files[i]

    dp = [[0 for i in range(K)] for j in range(K)]

    for length in range(2, K + 1):
        for i in range(K - length + 1):
            j = i + length - 1
            dp[i][j] = float("inf")

            for m in range(i, j):
                cost = dp[i][m] + dp[m + 1][j] + (prefix_sum[j + 1] - prefix_sum[i])
                dp[i][j] = min(dp[i][j], cost)

    return dp[0][K - 1]


# Read input
T = int(input().strip())

for _ in range(T):
    K = int(input().strip())
    files = list(map(int, input().split()))

    print(min_merge_cost_dp(K, files))

# 주석------------
# print(f"time : {time.time() - start:.5f} sec")
# ---------------
