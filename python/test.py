import time
import sys

# 주석------------
sys.stdin = open('python.txt', 'r')
start = time.time()
#----------------

N = int(sys.stdin.readline())
list_n = list(map(int, sys.stdin.readline().split(" ")))
M = int(sys.stdin.readline())
list_m = list(map(int, sys.stdin.readline().split(" ")))

answer = []

count = {}
for i in list_n:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

for i in list_m:
    result = count.get(i)
    if result == None:
        print(0, end=" ")
    else:
        print(result, end=" ")
        
# 주석------------
print("time : ", time.time() - start)
#----------------