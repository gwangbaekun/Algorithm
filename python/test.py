import sys
import time

# 주석------------
sys.stdin = open('python.txt', 'r')
start = time.time()
#----------------

N, B = map(int, sys.stdin.readline().split(" "))
metrix = []
for _ in range(N):
    metrix.append(list(map(int, sys.stdin.readline().split(" "))))

def multiply(metrix_a, metrix_b):
    global N
    arr = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                arr[i][j] += metrix_a[i][k] * metrix_b[k][j]

    for i in range(N):
        for j in range(N):
            arr[i][j] = arr[i][j] % 1000

    return arr

def reculsive(A, b):
    global metrix
    if b == 1:
        for i in range(N):
            for j in range(N):
                A[i][j] = A[i][j] % 1000
        return A
    
    tmp = reculsive(A, b//2)
    if b % 2:
        return multiply(multiply(tmp, tmp), A)
    else:
        return multiply(tmp, tmp)
    
result = reculsive(metrix, B)

for elem in result:
    print(*elem)
    
# 주석------------
print(f"time : {time.time() - start:.5f} sec")
# ---------------