import sys
import time

# 주석------------
# sys.stdin = open("/Users/jeyeolbaek/Developer/study/Algorithm/python/python.txt", "r")
# start = time.time()
# ----------------
input = sys.stdin.readline
# ----------------


def dp(index, weight_diff):
    # print(index, weight_diff, memo)

    if (index, weight_diff) in memo:
        return
    memo.add((index, weight_diff))

    if index == N:
        return

    dp(index + 1, weight_diff + weights[index])
    dp(index + 1, abs(weight_diff - weights[index]))
    dp(index + 1, weight_diff)
    dp(index + 1, weights[index])


N = int(input())
weights = list(map(int, input().split()))
M = int(input())
check_weight = list(map(int, input().split()))

memo = set()
dp(0, 0)

result = []
for cw in check_weight:
    result.append("Y" if any(cw == diff for _, diff in memo) else "N")

print(" ".join(result))

# 주석------------
# print(f"time : {time.time() - start:.5f} sec")
# ---------------
