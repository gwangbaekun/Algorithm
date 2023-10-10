import sys
import time

# 주석------------
sys.stdin = open('/Users/home/Developer/study/Algorithm/python/python.txt', 'r')
start = time.time()
#----------------

maxNum = 0
row, column = 1, 1

for i in range(9):
    nums = list(map(int, sys.stdin.readline().split()))
    if maxNum < max(nums):
        column = nums.index(max(nums)) + 1
        row =  i + 1
        maxNum = max(nums)

print(maxNum)
print(row, column)

# 주석------------
print(f"time : {time.time() - start:.5f} sec")
# ---------------

