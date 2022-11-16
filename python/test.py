import sys
import time
# 주석------------
# sys.stdin = open('python.txt', 'r')
# start = time.time()
#----------------

N, M = map(int, sys.stdin.readline().split(" "))

def counter(n, variable):
    count = 1
    divided_by_viriable = 0
    while n >= variable:
        if n // variable ** count == 0:
            break
        else:
            divided_by_viriable += (n // variable ** count)
        count += 1
    return divided_by_viriable

fives = counter(N, 2) - counter(M, 2) - counter(N-M, 2)
twos = counter(N, 5) - counter(M, 5) - counter(N-M, 5)

print(min(fives, twos))

# 주석------------
# print("time : ", time.time() - start)
# ----------------