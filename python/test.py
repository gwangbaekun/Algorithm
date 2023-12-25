import sys
import time

# 주석------------
# sys.stdin = open('/Users/home/Developer/study/Algorithm/python/python.txt', 'r')
# start = time.time()
#----------------

def func(n):

    if n == 1:
        return ['*']

    Stars = func(n//3)
    L = []
    for star in Stars:
        L.append(star * 3)
    for star in Stars:
        L.append(star + ' ' * (n // 3) + star)
    for star in Stars:
        L.append(star * 3)


    return L

N = int(sys.stdin.readline())
print("\n".join(func(N)))

# 주석------------
# print(f"time : {time.time() - start:.5f} sec")
# ---------------
