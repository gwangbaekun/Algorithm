import time
import sys
from collections import Counter

# 주석------------
sys.stdin = open('python.txt', 'r')
start = time.time()
#----------------
N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline().strip()) for _ in range(N)]

def mean(nums):
    return round(sum(nums)/len(nums))

def median(nums):
    nums.sort()
    mid = nums[len(nums)//2] # nums의 개수는 홀수
    
    return mid

def mode(nums):
    mode_dict = Counter(nums)
    modes = mode_dict.most_common()    
    
    if len(nums) > 1 : 
        if modes[0][1] == modes[1][1]:
            mod = modes[1][0]
        else : 
            mod = modes[0][0]
    else : 
        mod = modes[0][0]

    return mod
        
def scope(nums):
    return max(nums) - min(nums)

print(mean(nums))
print(median(nums))
print(mode(nums))
print(scope(nums))

# 주석------------
print("time : ", time.time() - start)
#----------------
