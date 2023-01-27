import sys
import time

# 주석------------
sys.stdin = open('python.txt', 'r')
start = time.time()
#----------------

N, M = map(int, sys.stdin.readline().split(" "))
arr = []
sum_arr = [[0 for _ in range(N + 1)] for _ in range(N + 1)]


for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split(" "))))

sum_arr[1][1] = arr[0][0]

def procession_sum(arr):
    for i in range(1, len(arr) + 1):
        for j in range(1, len(arr) + 1):
            sum_arr[i][j] = sum_arr[i - 1][j] + sum_arr[i][j - 1] + arr[i - 1][j - 1] - sum_arr[i - 1][j - 1]
    return sum_arr

sum_arr = procession_sum(arr)

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split(" "))
    print(sum_arr[x2][y2] - sum_arr[x2][y1 - 1] - sum_arr[x1 - 1][y2] + sum_arr[x1 - 1][y1 - 1])

# 주석------------
print(f"time : {time.time() - start:.5f} sec")
# ---------------