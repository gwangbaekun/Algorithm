import sys
import time
import heapq

# 주석------------
sys.stdin = open("/Users/jeyeolbaek/Developer/study/Algorithm/python/python.txt", "r")
start = time.time()
# ----------------
input = sys.stdin.readline
# ----------------

N = int(input())
dq = []

for _ in range(N):
    n = int(input())

    if n != 0:
        heapq.heappush(dq, (abs(n), n))

    else:
        if len(dq) == 0:
            print(0)
        else:
            abs_val, original_value = heapq.heappop(dq)
            print(original_value)


# 주석------------
print(f"time : {time.time() - start:.5f} sec")
# ---------------
