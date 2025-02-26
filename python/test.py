import sys
import time

# 주석------------
# sys.stdin = open("/Users/jeyeolbaek/Developer/study/Algorithm/python/python.txt", "r")
# start = time.time()
# ----------------
input = sys.stdin.readline
# ----------------

N = int(input())
l = list(map(int, input().split(" ")))

result = [l[0]]


def find_place(elem):
    start = 0
    end = len(result) - 1

    while start <= end:
        mid = (start + end) // 2

        if elem == result[mid]:
            return mid
        elif elem < result[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return start


for i in range(N):
    if l[i] > result[-1]:
        result.append(l[i])
    else:
        idx = find_place(l[i])
        result[idx] = l[i]

print(len(result))


# 주석------------
# print(f"time : {time.time() - start:.5f} sec")
# ---------------
