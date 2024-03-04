import sys
import time

# 주석------------
# sys.stdin = open('/Users/jeyeolbaek/Developer/study/Algorithm/python/python.txt', 'r')
# start = time.time()
#----------------
input = sys.stdin.readline
#----------------

N, M = map(int, input().split())
arr = list(map(int, input().split()))

sumArr = [0] * (N+1)
for i in range(1, N + 1):
    sumArr[i] = sumArr[i-1] + arr[i - 1]

for _ in range(M):
    i, j = map(int, input().split())
    print(sumArr[j] - sumArr[i-1])

# 주석------------
# print(f"time : {time.time() - start:.5f} sec")
# ---------------