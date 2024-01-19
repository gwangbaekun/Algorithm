import sys
import time

# 주석------------
sys.stdin = open('/Users/jeyeolbaek/Developer/study/Algorithm/python/python.txt', 'r')
start = time.time()
#----------------
input = sys.stdin.readline
#----------------

N = int(input())
print(N * N - N)

# 주석------------
print(f"time : {time.time() - start:.5f} sec")
# ---------------
