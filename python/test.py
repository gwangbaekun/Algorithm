import time
import sys

# 주석------------
# sys.stdin = open('python.txt', 'r')
# start = time.time()
#----------------

N, M = map(int,sys.stdin.readline().split())

scores = list(map(int, sys.stdin.readline().split()))

scores.sort()

print(scores[-M:][0])

# 주석------------
# print("time : ", time.time() - start)
#----------------
