import sys
import time

# 주석------------
sys.stdin = open('/Users/home/Developer/study/Algorithm/python/python.txt', 'r')
start = time.time()
#----------------

N, M = map(int, sys.stdin.readline().split())

def gcd(a, b):
    if a < b:
        a, b = a, b
    if b == 0:
        return a
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
    
def lcm(a, b):
    return a * b // gcd(a, b)

print(lcm(a, b))

# 주석------------
print(f"time : {time.time() - start:.5f} sec")
# ---------------
