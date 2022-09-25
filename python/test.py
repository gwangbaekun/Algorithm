import sys
import time
# 주석------------
# sys.stdin = open('python.txt', 'r')
# start = time.time()
#----------------

N = int(sys.stdin.readline())

for i in range(N):
    a = list(map(int, sys.stdin.readline().split(" ")))
    start = a[:2]
    end = a[2:]

    start_point_count = 0
    end_point_count = 0

    for i in range(int(sys.stdin.readline())):
        a = list(map(int, sys.stdin.readline().split(" ")))
        status_start = None
        status_end = None
        if (start[0] - a[0]) ** 2 + (start[1] - a[1]) ** 2 < a[2] ** 2:
            status_start = True
            start_point_count += 1
        if (end[0] - a[0]) ** 2 + (end[1] - a[1]) ** 2 < a[2] ** 2:
            status_end = True
            end_point_count += 1

        if status_start and status_end:
            start_point_count -= 1
            end_point_count -= 1
    
    print(start_point_count + end_point_count)

# 주석------------
# print("time : ", time.time() - start)
#----------------