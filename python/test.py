import sys
import time

# 주석------------
sys.stdin = open('python.txt', 'r')
start = time.time()
#----------------

str = sys.stdin.readline().strip()
bomb = sys.stdin.readline().strip()

len_bomb = len(bomb)
stack = []
previous = ''

for char in str:
    stack.append(char)
 
    if "".join(stack[-len_bomb:]) == bomb:
        for _ in range(len_bomb):
            stack.pop()

if len(stack) == 0:
    print("FRULA")
else:
    print("".join(stack))

# 주석------------
print(f"time : {time.time() - start:.5f} sec")
# ---------------