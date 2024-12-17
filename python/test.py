import sys
import time

# 주석------------
sys.stdin = open('/Users/jeyeolbaek/Developer/study/Algorithm/python/python.txt', 'r')
start = time.time()
#----------------
input = sys.stdin.readline
#----------------

N, M = map(int, input().split())
r = []
visited = [False] * N

def dfs():
    if len(r) == M:
        print(' '.join(map(str, r)))
        return
    
    for i in range(N):
        if visited[i]:
            continue

        visited[i] = True
        r.append(i + 1)
        dfs()
        r.pop()
        print(r)
        print(visited)
        visited[i] = False

dfs()


# 주석------------
print(f"time : {time.time() - start:.5f} sec")
# ---------------