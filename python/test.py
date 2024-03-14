import sys
import time

# 주석------------
sys.stdin = open('/Users/jeyeolbaek/Developer/study/Algorithm/python/python.txt', 'r')
start = time.time()
#----------------
input = sys.stdin.readline
#----------------

N, K = map(int, input().strip().split())
c_t = [int(input()) for _ in range(N)]

c_t.sort(reverse=True)

c_c = 0

for i in range(N):
    if K == 0:
        break
    if K >= c_t[i]:
        c_c += K // c_t[i]
        K = K % c_t[i] 

print(c_c)  
# 주석------------
print(f"time : {time.time() - start:.5f} sec")
# ---------------