import sys
import time

# 주석------------
# sys.stdin = open("/Users/jeyeolbaek/Developer/study/Algorithm/python/python.txt", "r")
# start = time.time()
# ----------------
input = sys.stdin.readline
sys.setrecursionlimit(300000)
# ----------------

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    if x == N - 1 and y == M - 1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < M and l[nx][ny] < l[x][y]:
            dp[x][y] += dfs(nx, ny)

    return dp[x][y]


N, M = map(int, input().split())
l = []
dp = [[-1] * M for _ in range(N)]
valid = 0

for _ in range(N):
    l.append(list(map(int, input().split())))

print(dfs(0, 0))

# 주석------------
# print(f"time : {time.time() - start:.5f} sec")
# ---------------
