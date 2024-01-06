import sys
import time
from collections import deque

# 주석------------
sys.stdin = open('/Users/home/Developer/study/Algorithm/python/python.txt', 'r')
start = time.time()
input = sys.stdin.readline
#----------------

def dfs(depth, curIdx):
    global res
    if depth == N // 2:
        A = 0
        B = 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    A += board[i][j]
                elif not visited[i] and not visited[j]:
                    B += board[i][j]
        res = min(res, abs(A - B))
        return
    for i in range(curIdx, N):
        if not visited[i]:
            visited[i] = 1
            dfs(depth + 1, curIdx + 1)
            visited[i] = 0

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [0 for _ in range(N)]
INF = 2147000000
res = INF

dfs(0, 0)
print(res)

# 주석------------
print(f"time : {time.time() - start:.5f} sec")
# ---------------
