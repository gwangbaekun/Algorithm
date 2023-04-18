import sys
import time
from collections import deque

# 주석------------
sys.stdin = open('/Users/home/Developer/study/Algorithm/python/python.txt', 'r')
start = time.time()
#----------------

N = int(sys.stdin.readline())
input = list(map(int, sys.stdin.readline().split(" ")))

# 인덱스로 넣을것임
stack = deque()

answer = [-1 for _ in range(N)]

for i in range(N):
    while len(stack) != 0 and input[stack[-1]] < input[i]:
        decidedIndex = stack.pop()
        answer[decidedIndex] = input[i]
    stack.append(i)

print(" ".join(map(str, answer)))

# 주석------------
print(f"time : {time.time() - start:.5f} sec")
# ---------------