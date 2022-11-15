import sys
import time
# 주석------------
# sys.stdin = open('python.txt', 'r')
# start = time.time()
#----------------

N = int(sys.stdin.readline())

print(N // 5 + N // 25 + N // 125)

# 주석------------
# print("time : ", time.time() - start)
# ----------------