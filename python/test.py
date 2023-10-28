import sys
import time

# 주석------------
sys.stdin = open('/Users/home/Developer/study/Algorithm/python/python.txt', 'r')
start = time.time()
#----------------

N, M = map(int, sys.stdin.readline().split())
cards = list(map(int,sys.stdin.readline().split()))
result = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            sum = cards[i] + cards[j] + cards[k]
            if sum <= M:
                result = max(result, sum)

print(result)

# 주석------------
print(f"time : {time.time() - start:.5f} sec")
# ---------------

