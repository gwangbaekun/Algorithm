import sys
import time

# 주석------------
# sys.stdin = open('/Users/jeyeolbaek/Developer/study/Algorithm/python/python.txt', 'r')
# start = time.time()
#----------------
input = sys.stdin.readline
#----------------

N = int(input())
A = set(map(int, input().split(" ")))
M = int(input())
a = list(map(int, input().split(" ")))

for i in range(M):
    if a[i] in A:
        print(1)
    else:
        print(0)


# 주석------------
# print(f"time : {time.time() - start:.5f} sec")
# ---------------