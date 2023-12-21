import sys
import time
from collections import deque

# 주석------------
sys.stdin = open('/Users/home/Developer/study/Algorithm/python/python.txt', 'r')
start = time.time()
#---------------- = 0

def recursion(s, l, r, count):
    if l >= r:
        return 1, count + 1
    elif s[l] != s[r]:
        return 0, count + 1
    else:
        count += 1
        return recursion(s, l+1, r-1, count)
    
def isPalindrome(s, count):
    return recursion(s, 0, len(s)-1, count)

N = int(sys.stdin.readline())

for _ in range(N):
    s = sys.stdin.readline().strip()
    print(isPalindrome(s, 0)[0], isPalindrome(s, 0)[1])
# 주석------------
print(f"time : {time.time() - start:.5f} sec")
# ---------------
