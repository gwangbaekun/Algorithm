import sys
import time

# 주석------------
# sys.stdin = open('python.txt', 'r')
# start = time.time()
#----------------

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split(" "))))

blue_count = 0
white_count = 0

def define_array_color(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 0:
                return False
    return True

def define_array(arr):
    status = arr[0][0]
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != status:
                return False
    return True

def cut(arr):
    num = int(len(arr)/2)
    result = [[] for _ in range(4)]
    for i in range(len(arr)):
        if i < num:
            result[0].append(arr[i][0:num])
            result[1].append(arr[i][num:len(arr)])
        else:
            result[2].append(arr[i][0:num])
            result[3].append(arr[i][num:len(arr)])

    return result

def reculsive(arr):
    global blue_count, white_count
    # first if it is all
        
    if define_array(arr):
        if define_array_color(arr):
            blue_count += 1
        else:
            white_count += 1            
        return 

    for elem in cut(arr):
        reculsive(elem)

# reculsive(arr)
reculsive(arr)

print(white_count,blue_count)

# 주석------------
# print(f"time : {time.time() - start:.5f} sec")
# ---------------