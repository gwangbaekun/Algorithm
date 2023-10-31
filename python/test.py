import sys
import time

# 주석------------
sys.stdin = open('/Users/home/Developer/study/Algorithm/python/python.txt', 'r')
start = time.time()
#----------------

N = int(sys.stdin.readline())

def get_number_sum(n):
    sum = 0
    for i in range(len(str(n))):
        sum += int(str(n)[i])
    return sum + n

for i in range(N):
    if get_number_sum(i) == N:
        print(i)
        break
    if i == N-1:
        print(0)


# 주석------------
print(f"time : {time.time() - start:.5f} sec")
# ---------------

