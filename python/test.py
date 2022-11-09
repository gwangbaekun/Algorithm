import sys
import time
# 주석------------
# sys.stdin = open('python.txt', 'r')
# start = time.time()
#----------------

N = int(sys.stdin.readline())

cases = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]

def factorial(N):
    if N == 0:
        return 1
    return N * factorial(N-1)

for i in cases:
    N, M = i[0], i[1]
    print(factorial(M) // factorial(M-N) // factorial(N))

# 주석------------
# print("time : ", time.time() - start)
# ----------------