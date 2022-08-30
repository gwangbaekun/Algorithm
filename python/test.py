import time
import sys

# 주석------------
# sys.stdin = open('python.txt', 'r')
# start = time.time()
#----------------

N = int(sys.stdin.readline())
have_list = list(map(int, sys.stdin.readline().split(" ")))
M = int(sys.stdin.readline())
check_list = list(map(int, sys.stdin.readline().split(" ")))

have_list.sort()

def binary_tree(start, end, list, element):
    while start <= end:
        mean = (start + end) // 2
        if element == list[mean]:
            return mean
        elif element < list[mean]:
            end = mean - 1
        else:
            start = mean + 1
    return None

for i in range(M):
    if binary_tree(0, N-1, have_list, check_list[i]) is None:
        print(0, end=" ")
    else:
        print(1, end=" ")

# 주석------------
# print("time : ", time.time() - start)
#----------------