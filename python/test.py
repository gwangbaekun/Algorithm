import sys
import time
# 주석------------
# sys.stdin = open('python.txt', 'r')
# start = time.time()
#----------------

N = int(sys.stdin.readline())

modify = list(map(int, sys.stdin.readline().split()))

a = 1

for i in range(N):
    a *= modify[i]

print(round(a ** (1/(N/2))))

# 주석------------
# print("time : ", time.time() - start)
# ----------------