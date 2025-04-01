import sys
import time

# 주석------------
# sys.stdin = open("/Users/jeyeolbaek/Developer/study/Algorithm/python/python.txt", "r")
# start = time.time()
# ----------------
input = sys.stdin.readline
# ----------------


def min_merge_cost_dp(K, l):
    dp = [[0 for i in range(K)] for j in range(K)]

    for length in range(2, K + 1):
        for i in range(K - length + 1):
            j = i + length - 1

            dp[i][j] = float("inf")

            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + l[i][0] * l[k][1] * l[j][1]
                if cost < dp[i][j]:
                    dp[i][j] = cost

    return dp[0][K - 1]


K = int(input().strip())
l = []
for _ in range(K):
    l.append(list(map(int, input().split())))

print(min_merge_cost_dp(K, l))

# 주석------------
# print(f"time : {time.time() - start:.5f} sec")
# ---------------
