import sys
import time
# 주석------------
# sys.stdin = open('python.txt', 'r')
# start = time.time()
#----------------

N = int(sys.stdin.readline())

def gcd(a, b):
    return b > 0 and gcd(b, a % b) or a

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split(" "))
    print(a * b // gcd(a, b))

# 주석------------
# print("time : ", time.time() - start)
# ----------------