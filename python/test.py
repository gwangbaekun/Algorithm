import sys
import time
import copy

# 주석------------
sys.stdin = open('python.txt', 'r')
start = time.time()
#----------------
            
N = int(input())

reculsive_count = 0
dynamic_count = 0

def reculsive_fib(n):
    global reculsive_count
    if n == 1 or n == 2:
        reculsive_count += 1
        return 1
    else:
        return reculsive_fib(n - 1) + reculsive_fib(n - 2)

def dynamic_fib(n):
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 1
    global dynamic_count
    for i in range(3, n+1):
        dynamic_count += 1
        dp[i] = dp[i - 1] + dp[i - 2]

dynamic_fib(N)
reculsive_fib(N)

print(reculsive_count, dynamic_count)

# 주석------------
print("time : ", time.time() - start)
# ---------------