import sys
import time

# 주석------------
sys.stdin = open('/Users/home/Developer/study/Algorithm/python/python.txt', 'r')
start = time.time()
#----------------

N = int(sys.stdin.readline())

dume = []
num = 0

while len(dume) < N:
    if '666' in str(num):
        dume.append(num)
        num += 1
    else:
        num += 1

print(dume[-1])

# 주석------------
print(f"time : {time.time() - start:.5f} sec")
# ---------------
