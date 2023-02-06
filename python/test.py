import sys
import time

# 주석------------
# sys.stdin = open('python.txt', 'r')
# start = time.time()
#----------------

N, K = map(int, sys.stdin.readline().split(" "))
p = 1000000007

# 팩토리얼 값 계산(나머지 연산 적용)
def factorial(N):
    n = 1
    for i in range(2, N+1):
        n = (n * i) % p
    return n

def square(n, k):
    if k == 0:
        return 1
    elif k == 1:
        return n

    tmp = square(n, k // 2)

    if k % 2:
        return tmp * tmp * n % p
    else:
        return tmp * tmp % p

top = factorial(N)
bottom = factorial(N - K) * factorial(K) % p

print(top * square(bottom, p-2) % p)

# 주석------------
# print(f"time : {time.time() - start:.5f} sec")
# ---------------