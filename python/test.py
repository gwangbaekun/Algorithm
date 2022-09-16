import time
import sys
# 주석------------
sys.stdin = open('python.txt', 'r')
start = time.time()
#----------------

x, y, w, h = map(int, input().split())

print(min(x, y, w-x, h-y))

# 주석------------
print("time : ", time.time() - start)
#----------------