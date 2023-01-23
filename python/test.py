import sys
import time

# 주석------------
# sys.stdin = open('python.txt', 'r')
# start = time.time()
#----------------

A, B = map(int, sys.stdin.readline().split(" "))
arr = list(map(int, sys.stdin.readline().split(" ")))

total = []
total.append(sum(arr[:B]))

for i in range(A - B):
    total.append(total[i] - arr[i] + arr[B + i])
    
print(max(total))
# 주석------------
# print(f"time : {time.time() - start:.5f} sec")
# ---------------