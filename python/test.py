import sys
import time

# 주석------------
# sys.stdin = open('python.txt', 'r')
# start = time.time()
#----------------

N = int(sys.stdin.readline())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

result = []

for i in A:
    count = 0
    for j in A:
        if (i[0] < j[0] and i[1] < j[1]):
            count += 1
    result.append(count + 1)

for rank in result:
    print(rank, end=" ")
# 주석------------
# end = time.time()
# print(f"{end - start:.5f} sec")
#----------------
