import sys
import time
from math import gcd
# 주석------------
# sys.stdin = open('python.txt', 'r')
# start = time.time()
#----------------

N = int(sys.stdin.readline())
arr = []
to_gcd = 0

for i in range(N):
    arr.append(int(sys.stdin.readline()))
    if i == 1:
        to_gcd = abs(arr[i] - arr[0])
    to_gcd = gcd(abs(arr[i] - arr[i - 1]), to_gcd)

gcd_squ = int(to_gcd ** 0.5)

answer = []

for i in range(2, gcd_squ + 1):
    if to_gcd % i == 0:
        answer.append(i)
        answer.append(to_gcd // i)
answer.append(to_gcd)
answer = list(set(answer))

answer.sort()

for i in answer:
    print(i, end=" ")
    
# 주석------------
# print("time : ", time.time() - start)
# ----------------