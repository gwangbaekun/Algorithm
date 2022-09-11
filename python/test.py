import time
import sys

# 주석------------
# sys.stdin = open('python.txt', 'r')
# start = time.time()
#----------------

N, M = map(int, sys.stdin.readline().split(" "))
A = set(map(int, sys.stdin.readline().split(" ")))

B = set(map(int, sys.stdin.readline().split(" ")))

result = sorted(list(A & B))

print(N + M - 2 * len(result))

# 주석------------
# print("time : ", time.time() - start)
#----------------