import sys
import math
import time

# 주석------------
sys.stdin = open('python.txt', 'r')
start = time.time()
#----------------

case = int(sys.stdin.readline())

for _ in range(case):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())


    floorList = [i+1 for i in range(n)]
    for _ in range(k):
        beforeHand = 0
        for i in range(len(floorList)):
            beforeHand += floorList[i]
            floorList[i] = beforeHand
    print(floorList[-1])


# 주석------------
end = time.time()
print(f"{end - start:.5f} sec")
#----------------
