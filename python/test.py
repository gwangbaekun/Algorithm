import sys
import time

# 주석------------
# sys.stdin = open("/Users/jeyeolbaek/Developer/study/Algorithm/python/python.txt", "r")
# start = time.time()
# ----------------
input = sys.stdin.readline
# ----------------

N = int(input())
t = list(map(int, input().split(" ")))
t.sort()

for i in range(N):
    if i > 0:
        t[i] = t[i] + t[i - 1]

print(sum(t))
# 주석------------
# print(f"time : {time.time() - start:.5f} sec")
# ---------------
