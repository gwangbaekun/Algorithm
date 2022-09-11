import time
import sys
# 주석------------
sys.stdin = open('python.txt', 'r')
# start = time.time()
#----------------

S = input()

_set = set()

for i in range(len(S)):
    for j in range(i, len(S)):
        _set.add(S[i:j+1])

print(len(_set))

# 주석------------
# print("time : ", time.time() - start)
#----------------