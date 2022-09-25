import sys
import time
# 주석------------
sys.stdin = open('python.txt', 'r')
start = time.time()
#----------------

W,H,X,Y,P = list(map(int ,sys.stdin.readline().split(" ")))

count = 0

for _ in range(P):
    a, b = list(map(int, sys.stdin.readline().split(" ")))
    # in square ?
    if a >= X and a <= X+W and b >= Y and b <= Y+H:
        count += 1
    # X, Y+H/2
    elif (X - a) ** 2 + (Y + H/2 - b) ** 2 <= (H/2) ** 2:
        count += 1
    elif (X + W - a) ** 2 + (Y + H/2 - b) ** 2 <= (H/2) ** 2:
        count += 1

print(count)
# 주석------------
print("time : ", time.time() - start)
# ----------------