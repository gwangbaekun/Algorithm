import sys
import time

# 주석------------
sys.stdin = open("/Users/jeyeolbaek/Developer/study/Algorithm/python/python.txt", "r")
start = time.time()
# ----------------
input = sys.stdin.readline
# ----------------

N = int(input())
meetings = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

meetings.sort(key=lambda x: (x[1], x[0]))

count = 0
end_time = 0

for start, end in meetings:
    if start >= end_time:
        count += 1
        end_time = end

print(count)


# 주석------------
print(f"time : {time.time() - start:.5f} sec")
# ---------------
