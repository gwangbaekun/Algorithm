import sys
import time

# 주석------------
sys.stdin = open('/Users/home/Developer/study/Algorithm/python/python.txt', 'r')
start = time.time()
#----------------

prime = []
check = [0] * 1000001
check[0] = 1
check[1] = 1

for i in range(2, 1000001):
    if check[i] == 0:
        prime.append(i)
        for j in range(2*i, 1000001, i):
            check[j] = 1

N = int(sys.stdin.readline())

for _ in range(N):
    count = 0
    n = int(sys.stdin.readline())
    for i in prime:
        if i > n:
            break
        if check[n - i] == 0 and i <= n - i:
            count += 1
    print(count)

# 주석------------
print(f"time : {time.time() - start:.5f} sec")
# ---------------
