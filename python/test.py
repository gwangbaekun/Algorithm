import sys
import time

# 주석------------
# sys.stdin = open('/Users/jeyeolbaek/Developer/study/Algorithm/python/python.txt', 'r')
# start = time.time()
#----------------
input = sys.stdin.readline
#----------------

N, M, K = map(int, input().split())

print(N + M + K)


# 주석------------
# print(f"time : {time.time() - start:.5f} sec")
# ---------------