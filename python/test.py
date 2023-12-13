import sys
import time

# 주석------------
sys.stdin = open('/Users/home/Developer/study/Algorithm/python/python.txt', 'r')
start = time.time()
#----------------

N = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
stack = []
cnt = 1

while l:
    if cnt == l[0]:
        l.pop(0)
        cnt += 1
    else:
        stack.append(l.pop(0))

    while stack:
        if stack[-1] == cnt:
            stack.pop()
            cnt += 1
        else:
            break

if len(stack) == 0:
    print("Nice")
else:
    print("Sad")

# 주석------------
print(f"time : {time.time() - start:.5f} sec")
# ---------------
