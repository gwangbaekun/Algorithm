import sys
import time
import copy


# 주석------------
sys.stdin = open('python.txt', 'r')
start = time.time()
#----------------
r = sys.stdin.readline
N = int(r())

for _ in range(N):
    n = int(r())
    seq = [1,1,1,2,2]

    for i in range(5, n):
        seq.append(seq[i - 1] + seq[i - 5])

    print(seq[n-1])

# 주석------------
print("time : ", time.time() - start)
# ---------------