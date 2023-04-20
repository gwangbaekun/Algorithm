import sys
import time
from collections import deque

# 주석------------
# sys.stdin = open('/Users/home/Developer/study/Algorithm/python/python.txt', 'r')
# start = time.time()
#----------------

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split(" ")))

stack = deque()
numMap = {}
checkArr = [0 for _ in range(N)]
answer = [-1 for _ in range(N)]

for i in range(N):
    if nums[i] in numMap:
        numMap[nums[i]] += 1
    else:
        numMap[nums[i]] = 1

for i in range(N):
    checkArr[i] = numMap[nums[i]]

for i in range(N):
    while len(stack) != 0 and checkArr[stack[-1]] < checkArr[i]:
        tmp = stack.pop()

        answer[tmp] = nums[i]

    stack.append(i)

print(" ".join(map(str, answer)))

# 주석------------
# print(f"time : {time.time() - start:.5f} sec")
# ---------------