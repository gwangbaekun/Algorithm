import sys
import time

# 주석------------
# sys.stdin = open('python.txt', 'r')
# start = time.time()
#----------------

N, M = map(int, sys.stdin.readline().split(" "))
arr = list(map(int, sys.stdin.readline().split(" ")))
arr_re = [0 for _ in range(M)]
count = 0

for i in range(N):
    if i == 0:
        arr[0] = arr[0]
    else:
        arr[i] = arr[i - 1] + arr[i]

    remain = arr[i] % M

    if remain == 0:
        count += 1

    arr_re[remain] += 1

for i in range(M):
    count += arr_re[i] * (arr_re[i] - 1) / 2

print(int(count))
    
    

# 주석------------
# print(f"time : {time.time() - start:.5f} sec")
# ---------------