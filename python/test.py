import sys
import time

# 주석------------
sys.stdin = open('/Users/home/Developer/study/Algorithm/python/python.txt', 'r')
start = time.time()
#----------------

a,b,c,d,e,f = map(int, sys.stdin.readline().split())

if (a * e - d * b) == 0 or (b * d - e * a) == 0:
    x = (a + b) // c
    y = (a + b) // c
else:
    y = (c * d - f * a) // (b * d - e * a)
    x = (c * e - f * b) // (a * e - d * b)

print(x, y)


# 주석------------
print(f"time : {time.time() - start:.5f} sec")
# ---------------

