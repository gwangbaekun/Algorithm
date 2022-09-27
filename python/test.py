import sys
import time
# 주석------------
# sys.stdin = open('python.txt', 'r')
# start = time.time()
#----------------

while True:
    a, b = map(int, sys.stdin.readline().split())
    if (a == 0 and b == 0):
        break
    if (b % a == 0):
        print('factor')
    elif (a % b == 0):
        print('multiple')
    else:
        print('neither')
   
# 주석------------
# print("time : ", time.time() - start)
# ----------------