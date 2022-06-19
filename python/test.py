import sys
import math
import time

# 주석------------
sys.stdin = open('python.txt', 'r')
start = time.time()
#----------------

def is_prime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

while True:
    n = int(input())
    if n == 0:
        break
    count = 0
    for i in range(n + 1, 2 * n + 1):
        if is_prime(i):
            count += 1
    print(count)


# 주석------------
end = time.time()
print(f"{end - start:.5f} sec")
#----------------
