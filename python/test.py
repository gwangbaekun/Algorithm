import time
# 주석------------
sys.stdin = open('python.txt', 'r')
start = time.time()
#----------------

import sys
# C = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(3)]
dictX = {}
dictY = {}
for i in range(3):
    x, y = map(int, sys.stdin.readline().split(" "))
    if x in dictX:
        dictX[x] += 1
    else:
        dictX[x] = 1
    
    if y in dictY:
        dictY[y] += 1
    else:
        dictY[y] = 1

for key in dictX:
    if dictX[key] == 1:
        print(key, end=" ")

for key in dictY:
    if dictY[key] == 1:
        print(key)

# 주석------------
print("time : ", time.time() - start)
#----------------