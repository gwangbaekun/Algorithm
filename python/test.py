import sys
import time

# 주석------------
# sys.stdin = open('/Users/home/Developer/study/Algorithm/python/python.txt', 'r')
# start = time.time()
#----------------

nums = [int(sys.stdin.readline()) for _ in range(5)]

nums.sort()

print(sum(nums)//5, nums[2], sep='\n')

# 주석------------
# print(f"time : {time.time() - start:.5f} sec")
# ---------------
