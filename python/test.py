import sys
import time

# 주석------------
# sys.stdin = open('/Users/home/Developer/study/Algorithm/python/python.txt', 'r')
# start = time.time()
#----------------

N = int(sys.stdin.readline())

def isPrime(n):
    if n == 0:
        return False
    if n == 1:
        return False
    for i in range(2, int(n **0.5) + 1):
        if n % i == 0:
            return False
    return True
     
for _ in range(N):
    n = int(sys.stdin.readline())
    while not isPrime(n):
        n += 1
    print(n)
# 주석------------
# print(f"time : {time.time() - start:.5f} sec")
# ---------------
