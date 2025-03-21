import sys
import time
import heapq

# 주석------------
sys.stdin = open("/Users/jeyeolbaek/Developer/study/Algorithm/python/python.txt", "r")
start = time.time()
# ----------------
input = sys.stdin.readline
# ----------------


def min_merge_cost_dp(K, files):
    # Prefix sum to quickly get the sum of any range
    prefix_sum = [0] * (K + 1)
    for i in range(K):
        prefix_sum[i + 1] = prefix_sum[i] + files[i]

    # DP table
    dp = [[0] * K for _ in range(K)]

    # Solve for increasing subarray lengths
    for length in range(2, K + 1):  # length = 2 to K
        for i in range(K - length + 1):
            j = i + length - 1
            dp[i][j] = float("inf")

            # Try all possible partitions
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
print(f"time : {time.time() - start:.5f} sec")
# ---------------
