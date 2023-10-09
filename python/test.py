import sys
import time

# 주석------------
# sys.stdin = open('/Users/home/Developer/study/Algorithm/python/python.txt', 'r')
# start = time.time()
#----------------

pieces = [1, 1, 2, 2, 2, 8]
h = sys.stdin.readline().split(" ")

for i in range(0, len(h)):
    print(pieces[i] - int(h[i]), end=" ")

# 주석------------
# print(f"time : {time.time() - start:.5f} sec")
# ---------------

