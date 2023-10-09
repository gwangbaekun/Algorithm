import sys
import time

# 주석------------
# sys.stdin = open('/Users/home/Developer/study/Algorithm/python/python.txt', 'r')
# start = time.time()
#----------------

h = int(sys.stdin.readline())

for i in range(1, h + 1):
    print(' ' * (h - i) + '*' * (2 * i - 1))

for i in range(h - 1, 0, -1):
    print(' ' * (h - i) + '*' * (2 * i - 1))

# 주석------------
# print(f"time : {time.time() - start:.5f} sec")
# ---------------

