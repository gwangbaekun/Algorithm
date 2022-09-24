import sys
import time
import math
# 주석------------
# sys.stdin = open('python.txt', 'r')
# start = time.time()
#----------------

N = int(sys.stdin.readline())

print(round(math.pi * N * N, 6))
print("{:.6f}".format( 2 * N * N))

# 주석------------
# print("time : ", time.time() - start)
#----------------