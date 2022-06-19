import sys
import math
import time

# 주석------------
# sys.stdin = open('python.txt', 'r')
# start = time.time()
#----------------

case = int(sys.stdin.readline())

def isPrime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

for _ in range(case):
    n = int(sys.stdin.readline())
    a, b = n//2, n//2
    while a > 0:
        if isPrime(a) and isPrime(b):
            print(a, b)
            break
        a -= 1
        b += 1

# 주석------------
# end = time.time()
# print(f"{end - start:.5f} sec")
#----------------
