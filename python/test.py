import sys
import time

# 주석------------
# sys.stdin = open('/Users/jeyeolbaek/Developer/study/Algorithm/python/python.txt', 'r')
# start = time.time()
#----------------
input = sys.stdin.readline
#----------------

N, M = map(int, input().split())

visited = [False] * N

def dfs(n, temp):
    if len(temp) == M:
        print(" ".join(map(str, temp)))
        return
    
    for i in range(N):
        if visited[i] == False:
            temp.append(i + 1)
            visited[i] = True
            dfs(i + 1, temp)    
            temp.pop()
            visited[i] = False
    

dfs(0, [])


# 주석------------
# print(f"time : {time.time() - start:.5f} sec")
# ---------------