import sys
import time

# 주석------------
# sys.stdin = open('/Users/home/Developer/study/Algorithm/python/python.txt', 'r')
# start = time.time()
#----------------

A, B = map(int, sys.stdin.readline().split())
C, D = map(int, sys.stdin.readline().split())

def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a%b)

def lcm(a, b):
    return a * b // gcd(a, b)

def solution(a, b, c, d):
    lcmNum = lcm(b, d)
    a = a * (lcmNum // b)
    c = c * (lcmNum // d)
    return a + c, lcmNum

top, bottom = solution(A, B, C, D)

print(top // gcd(top,bottom), bottom // gcd(top,bottom))

# 주석------------
# print(f"time : {time.time() - start:.5f} sec")
# ---------------
