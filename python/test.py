import sys
import time

# 주석------------
# sys.stdin = open('/Users/jeyeolbaek/Developer/study/Algorithm/python/python.txt', 'r')
# start = time.time()
#----------------
input = sys.stdin.readline
#----------------

N = int(input())
nums = list(map(int, input().split()))
reverse_nums = nums[::-1]

increase = [0] * N
decrease = [0] * N

for i in range(N):
    for j in range(i):
        if nums[j] < nums[i]:
            increase[i] = max(increase[i], increase[j] + 1)
        if reverse_nums[j] < reverse_nums[i]:
            decrease[i] = max(decrease[i], decrease[j] + 1)

for i in range(N):
    increase[i] = increase[i] + decrease[N - i - 1]

print(max(increase) + 1)

# 주석------------
# print(f"time : {time.time() - start:.5f} sec")
# ---------------