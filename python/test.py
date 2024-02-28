import sys
import time

# 주석------------
# sys.stdin = open('/Users/jeyeolbaek/Developer/study/Algorithm/python/python.txt', 'r')
# start = time.time()
#----------------
input = sys.stdin.readline
#----------------

N, K = map(int, input().split())
stuffs = [list(map(int, input().split())) for _ in range(N)]

cache = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(0, K + 1):
        w, v = stuffs[i - 1]
        if w <= j:
            cache[i][j] = max(v + cache[i - 1][j - w], cache[i-1][j])
        else:
            cache[i][j] = cache[i-1][j]

print(cache[-1][-1])

# 주석------------
# print(f"time : {time.time() - start:.5f} sec")
# ---------------