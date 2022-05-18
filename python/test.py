import queue
import sys
from collections import deque

sys.stdin = open("python.txt", "r")

N = int(sys.stdin.readline())

graph = []
c = [[0]*N for _ in range(N)]

for _ in range(N):
    graph.append(list(map(str, sys.stdin.readline().strip())))

def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            
            if graph[nx][ny] == graph[x][y] and c[nx][ny] == 0:
                queue.append((nx,ny))
                c[nx][ny] = 1

cnt = 0
for i in range(N):
    for j in range(N):
        if c[i][j] == 0:
            bfs(i, j)
            print(c)    
            cnt += 1

print(cnt, end=" ")

for i in range(N):
    for j in range(N):
        if graph[i][j] == 'R':
            graph[i][j] = "G"

c = [[0]*N for _ in range(N)]
cnt = 0

for i in range(N):
    for j in range(N):
        if c[i][j] == 0:
            bfs(i,j)
            cnt += 1

print(cnt)