import sys
import time
from math import gcd

# 주석------------
sys.stdin = open('/Users/home/Developer/study/Algorithm/python/python.txt', 'r')
start = time.time()
#----------------

N = int(sys.stdin.readline())

a = int(sys.stdin.readline())    
arr = []
for _ in range(1, N):
    num = int(sys.stdin.readline())
    arr.append(num - a)
    a = num
        
g = arr[0]
for i in range(1, len(arr)):
    g = gcd(g, arr[i])

result = 0
for each in arr:
    result += each // g - 1

# 주석------------
print(f"time : {time.time() - start:.5f} sec")
# ---------------
