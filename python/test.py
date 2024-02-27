import sys
import time

# 주석------------
# sys.stdin = open('/Users/jeyeolbaek/Developer/study/Algorithm/python/python.txt', 'r')
# start = time.time()
#----------------
input = sys.stdin.readline
#----------------

char, char2 = input().strip(), input().strip()
l1, l2 = len(char), len(char2)
results = [[0] * (l2 + 1) for _ in range(l1 + 1)]
for i in range(1, l1 + 1):
    for j in range(1, l2 + 1):          
        if char[i-1] == char2[j-1]:
            results[i][j] = results[i-1][j-1] + 1
        else:
            results[i][j] = max(results[i-1][j], results[i][j-1])

print(results[-1][-1])

# 주석------------
# print(f"time : {time.time() - start:.5f} sec")
# ---------------