import time
import sys

# 주석------------
sys.stdin = open('python.txt', 'r')
start = time.time()
#----------------

N = int(sys.stdin.readline())

arr = []

for i in str(N):
    arr.append(int(i))

arr.sort(reverse=True)

for i in arr:
    print(i, end="")

# 주석------------
print("time : ", time.time() - start)
#----------------
