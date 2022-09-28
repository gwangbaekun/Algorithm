import sys
import time
# 주석------------
# sys.stdin = open('python.txt', 'r')
# start = time.time()
#----------------

A, B = map(int ,sys.stdin.readline().split(" "))

def gcd(a, b):
    return b > 0 and gcd(b, a % b) or a

g = gcd(A, B)
m = g * (A // g) * (B // g)

print(g )
print(m)

# 주석------------
# print("time : ", time.time() - start)
# ----------------