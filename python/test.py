import sys
import time

# 주석------------
sys.stdin = open('/Users/jeyeolbaek/Developer/study/Algorithm/python/python.txt', 'r')
start = time.time()
#----------------
input = sys.stdin.readline
#----------------

N = int(input())

s = ""

for _ in range(int(N / 4)):
    s += "long "

s += "int"

print(s)
# 주석------------
print(f"time : {time.time() - start:.5f} sec")
# ---------------