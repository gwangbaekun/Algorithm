import time
import sys

# 주석------------
# sys.stdin = open('python.txt', 'r')
# start = time.time()
#----------------

N = int(sys.stdin.readline())
nums = []
for i in range(N):
    nums.append(int(sys.stdin.readline().strip()))

nums.sort()

for i in nums:
    print(i)

# 주석------------
# print("time : ", time.time() - start)
#----------------
