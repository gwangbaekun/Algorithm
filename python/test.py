import sys
import math
import time

# 주석------------
# sys.stdin = open('python.txt', 'r')
# start = time.time()
#----------------

N = int(sys.stdin.readline())
d = 2
sqrt = int(math.sqrt(N))

while d <= sqrt:
    if N % d != 0:
        d += 1
    else:
        print(d)
        N //= d
if N > 1:
    print(N)

# 주석------------
# end = time.time()
# print(f"{end - start:.5f} sec")
#----------------
