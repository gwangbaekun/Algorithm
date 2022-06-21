import sys
import math
import time

# 주석------------
# sys.stdin = open('python.txt', 'r')
# start = time.time()
#----------------

N = int(sys.stdin.readline())

def multi(x):
    result = 1
    if x > 0:
        result = x * multi(x-1)
    return result

print(multi(N))

# 주석------------
# end = time.time()
# print(f"{end - start:.5f} sec")
#----------------
