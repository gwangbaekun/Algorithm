import sys
import time
from collections import deque 

# 주석------------
sys.stdin = open('python.txt', 'r')
start = time.time()
#----------------

N = int(sys.stdin.readline())

for _ in range(N):
    functions = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    arr = sys.stdin.readline().strip().strip('][').split(',')
    q = deque(arr)

    direction = 1
    count = 0

    for elem in functions:
        if elem == 'R':
            direction = -direction
            count += 1
        elif elem == 'D':
            if len(q) > 0:
                if direction == 1:
                    q.popleft()
                else:
                    q.pop()
    

    
    if len(functions) - count > n:
        print('error')
    else:
        if count % 2 == 1:
            q.reverse()
            print( '[' + ','.join(q) + ']')
        else:
            print( '[' + ','.join(q) + ']')

# 주석------------
print(f"time : {time.time() - start:.5f} sec")
# ---------------