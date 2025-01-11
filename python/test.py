import sys
import time

# 주석------------
# sys.stdin = open('/Users/jeyeolbaek/Developer/study/Algorithm/python/python.txt', 'r')
# start = time.time()
#----------------
input = sys.stdin.readline
#----------------

N = int(input())

dancing = {"ChongChong"}

for i in range(N):
    a, b = input().rstrip().split(" ")

    if a in dancing:
        dancing.add(b)

    if b in dancing:
        dancing.add(a)

print(len(dancing))

# 주석------------
# print(f"time : {time.time() - start:.5f} sec")
# ---------------