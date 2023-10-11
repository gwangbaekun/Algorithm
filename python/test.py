import sys
import time

# 주석------------
sys.stdin = open('/Users/home/Developer/study/Algorithm/python/python.txt', 'r')
start = time.time()
#----------------

strings = [list(sys.stdin.readline().rstrip()) for _ in range(5)]
maxString = 0

for i in range(len(strings)):
    if maxString < len(strings[i]):
        maxString = len(strings[i])

for j in range(maxString):
    for i in range(5):
        if len(strings[i]) > j:
            print(strings[i][j], end='')
        # print(strings[i][j], end='')

# for i in range(5):
#     print(strings[i][1], end='')


# 주석------------
# print(f"time : {time.time() - start:.5f} sec")
# ---------------

