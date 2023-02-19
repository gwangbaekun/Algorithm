import sys
import time

# 주석------------
# sys.stdin = open('python.txt', 'r')
# start = time.time()
#----------------

N, L = map(int, sys.stdin.readline().split(" "))
al = list(map(int, sys.stdin.readline().split(" ")))

al_blood = 0
count = 0
for i in range(len(al)):
    if i >= L:
        al_blood += al[i] - al[i - L]
    else:
        al_blood += al[i]

    if al_blood >= 129 and al_blood<= 138:
        count += 1

print(count)
# 주석------------
# print(f"time : {time.time() - start:.5f} sec")
# ---------------