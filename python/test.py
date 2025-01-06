import sys
import time

# 주석------------
sys.stdin = open('/Users/jeyeolbaek/Developer/study/Algorithm/python/python.txt', 'r')
start = time.time()
#----------------
input = sys.stdin.readline
#----------------

X = int(input())
N = int(input())

sum = 0

for _ in range(N):
    a, b = map(int, input().split())
    sum += a * b
 
if sum == X:
    print("Yes")
else:
    print("No")

# 주석------------
print(f"time : {time.time() - start:.5f} sec")
# ---------------