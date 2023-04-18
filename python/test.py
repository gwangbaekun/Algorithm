import sys
import time
from collections import deque

# 주석------------
sys.stdin = open('/Users/home/Developer/study/Algorithm/python/python.txt', 'r')
start = time.time()
#----------------

while True:
    recs = list(map(int, sys.stdin.readline().split(" ")))
    lenInput = recs[0]
    recs = recs[1:]
    if lenInput == 0:
        break

    stack = deque()
    area = 0

    for i in range(lenInput):
        while len(stack) != 0 and recs[stack[-1]] > recs[i]:
            tmp = stack.pop()
            
            if len(stack) == 0:
                width = i
            else:
                width = i - stack[-1] - 1
            
            area = max(area, width * recs[tmp])

        stack.append(i)

    while len(stack) != 0:
        tmp = stack.pop()

        if len(stack) == 0:
            width = lenInput
        else:
            width = lenInput - stack[-1] - 1

        area = max(area, width * recs[tmp])

    print(area)
            

# 주석------------
print(f"time : {time.time() - start:.5f} sec")
# ---------------