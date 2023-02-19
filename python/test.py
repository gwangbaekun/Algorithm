import sys
import time
from collections import deque

# 주석------------
sys.stdin = open('python.txt', 'r')
start = time.time()
#----------------

N = int(sys.stdin.readline())
actions = []
answer = deque([])

for _ in range(N):
    action = list(sys.stdin.readline().split(" "))
    actions.append(action)

status = []

for action in actions:
    if action[0] == '1':
        answer.append(action[1].strip())
        status.append('1')
    elif action[0] == '2':
        answer.appendleft(action[1].strip())
        status.append('2')
    else:
        if len(status) != 0:
            if status[-1] == '1':
                answer.pop()
                status.pop()
            elif status[-1] == '2':
                answer.popleft()
                status.pop()

if len(answer) == 0:
    print(0)
else:
    print(''.join(answer))

# 주석------------
print(f"time : {time.time() - start:.5f} sec")
# ---------------