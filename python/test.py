import sys
import time

# 주석------------
# sys.stdin = open("/Users/jeyeolbaek/Developer/study/Algorithm/python/python.txt", "r")
# start = time.time()
# ----------------
input = sys.stdin.readline
# ----------------

N, M, K = map(int, input().split(" "))
result = 1
exp = M
base = N
while exp > 0:
    if exp % 2 == 1:
        result = result * base % K
    base = base * base % K
    exp //= 2

print(result)

# 주석------------
# print(f"time : {time.time() - start:.5f} sec")
# ---------------
