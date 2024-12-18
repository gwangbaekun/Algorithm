import sys
import time

# 주석------------
# sys.stdin = open('/Users/jeyeolbaek/Developer/study/Algorithm/python/python.txt', 'r')
# start = time.time()
#----------------
input = sys.stdin.readline
#----------------

N = int(input())
matrix = [[1,1], [1,0]]
mod = int(1E9 + 7)

def multiply(A, B):
    return [
        [(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % mod, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % mod],
        [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % mod, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % mod]
    ]

def power(A, n):
    if n == 1:
        return A
    if n % 2 == 0:
        route_arr = power(A, n // 2)
        return multiply(route_arr, route_arr)
    else:
        return multiply(power(A, n - 1), A)

def fibonacci(N):
    return power(matrix, N)[0][1]

print(fibonacci(N))

# 주석------------
# print(f"time : {time.time() - start:.5f} sec")
# ---------------