import sys
import time

# 주석------------
# sys.stdin = open('/Users/home/Developer/study/Algorithm/python/python.txt', 'r')
# start = time.time()
#----------------

coordinates = [[0 for _ in range(100)] for _ in range(100)]

N = int(sys.stdin.readline())
papers = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for paper in papers:
    for i in range(paper[0], paper[0]+10):
        for j in range(paper[1], paper[1]+10):
            coordinates[i][j] = 1

print(sum(sum(coordinates, [])))

# 주석------------
# print(f"time : {time.time() - start:.5f} sec")
# ---------------

