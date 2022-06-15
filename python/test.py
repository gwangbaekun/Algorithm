import sys
import time
# from hooks.isPrime import primenum

# 주석------------
# sys.stdin = open('python.txt', 'r')
# start = time.time()
#----------------

N = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))

def primenum(x):
    if x == 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

numCount = 0
for num in nums:
    if primenum(num):
        numCount += 1

print(numCount)
# print(int(math.sqrt(4) + 1))

# 주석------------
# end = time.time()
# print(f"{end - start:.5f} sec")
#----------------
