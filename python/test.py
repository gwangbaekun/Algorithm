import time
import sys

# 주석------------
# sys.stdin = open('python.txt', 'r')
# start = time.time()
#----------------

N = int(sys.stdin.readline())

to_sort = [list(sys.stdin.readline().split()) for _ in range(N)]

to_sort.sort(key=lambda x: int(x[0]))

for i in to_sort:
    print(" ".join(i))

# 주석------------
# print("time : ", time.time() - start)
#----------------