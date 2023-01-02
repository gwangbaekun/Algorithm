import sys
import time
import copy

# 주석------------
sys.stdin = open('python.txt', 'r')
start = time.time()
#----------------
            
N = int(input())
count = 0
row = [0] * N

def is_queen_possible(x):
    for i in range(x):
        if row[i] == row[x] or abs(x-i) == abs(row[x] - row[i]):
            return False

    return True

def dfs(index):
    global count
    if index == N:
        count += 1
        return

    else:
        for i in range(N):
            row[index] = i
            if is_queen_possible(index):
                dfs(index + 1)

dfs(0)

print(count)


# 주석------------
print("time : ", time.time() - start)
# ---------------