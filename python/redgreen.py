import sys
from collections import deque
# sys.stdin = open("python.txt", "r")
N = int(sys.stdin.readline())
board = [list(sys.stdin.readline().strip()) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

q = deque()
cnt = 0
c = [[0]*N for _ in range(N)]

def bfs(x, y):
    q.append([x,y])
    c[x][y] = cnt
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] == board[x][y] and c[nx][ny] == 0:
                    q.append([nx, ny])
                    c[nx][ny] = 1

for i in range(N):
    for j in range(N):
        if c[i][j] == 0:
            bfs(i,j)
            cnt += 1

print(cnt, end=" ")

for i in range(N):
    for j in range(N):
        if (board[i][j] == "R"):
            board[i][j] = 'G'

cnt = 0
c = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if c[i][j] == 0:
            bfs(i, j)
            cnt += 1

print(cnt)
