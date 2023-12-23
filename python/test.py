import sys
import time
from collections import deque

# 주석------------
# sys.stdin = open('/Users/home/Developer/study/Algorithm/python/python.txt', 'r')
# start = time.time()
#----------------

def kantor(strL, count):
    _strL = []
    if count == 0:
        return "".join(strL)
    else:
        for str in strL:
            onethird = 3 ** (count) // 3
            _strL.append(str[:onethird])
            _strL.append(" " * (3 ** (count - 1)))
            _strL.append(str[:onethird])
        return kantor(_strL, count - 1)

while True:
    try:
        N = int(sys.stdin.readline())
        print(kantor(["-"* (3 ** (N))], N))
    except:
        break

# 주석------------
# print(f"time : {time.time() - start:.5f} sec")
# ---------------
