import sys
import time

# 주석------------
sys.stdin = open('python.txt', 'r')
start = time.time()
#----------------

N, M = map(int ,sys.stdin.readline().split(" "))

s = []

def dfs():
    if (len(s) == M):
        print(" ".join(map(str, s)))
        return
    for i in range(1, N+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()

dfs()

# 주석------------
print("time : ", time.time() - start)
# ---------------