import sys
import time

# 주석------------
# sys.stdin = open('/Users/home/Developer/study/Algorithm/python/python.txt', 'r')
# start = time.time()
#----------------

N = int(sys.stdin.readline())
count = 0
check = 1
while check ** 2 <= N:
    check += 1
    count += 1

print(count)

# 주석------------
# print(f"time : {time.time() - start:.5f} sec")
# ---------------
