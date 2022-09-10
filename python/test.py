import time
import sys

# 주석------------
sys.stdin = open('python.txt', 'r')
# start = time.time()
#----------------

N, M = map(int, sys.stdin.readline().split(" "))
d = set()
for i in range(N):
    d.add(sys.stdin.readline().strip())

b = set()
for i in range(M):
    b.add(sys.stdin.readline().strip())

result = sorted(list(d & b))

print(len(result))
for i in result:
    print(i)

# 주석------------
# print("time : ", time.time() - start)
#----------------