import sys
import time
from collections import deque

# 주석------------
sys.stdin = open('/Users/home/Developer/study/Algorithm/python/python.txt', 'r')
start = time.time()
input = sys.stdin.readline
#----------------

max_val = -1e9 - 1
min_val = 1e9 + 1

def cal(depth, result, plus, minus, multi, div):
    global N, max_val, min_val
    if depth == N:
        max_val = max(max_val, result)
        min_val = min(min_val, result)
        return
    
    if plus:
        cal(depth+1, result+nums[depth], plus-1, minus, multi, div)
    if minus:
        cal(depth+1, result-nums[depth], plus, minus-1, multi, div)
    if multi:
        cal(depth+1, result*nums[depth], plus, minus, multi-1, div)
    if div:
        if result < 0:
            cal(depth+1, -(-result//nums[depth]), plus, minus, multi, div-1)
        else:
            cal(depth+1, result//nums[depth], plus, minus, multi, div-1)

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
plus, minus, multi, div = map(int, sys.stdin.readline().split())

cal(1, nums[0], plus, minus, multi, div)
print(int(max_val), int(min_val), sep='\n')

# 주석------------
print(f"time : {time.time() - start:.5f} sec")
# ---------------
