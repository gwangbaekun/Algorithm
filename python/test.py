import sys
import time
import copy

# 주석------------
sys.stdin = open('python.txt', 'r')
start = time.time()
#----------------

N = int(sys.stdin.readline())

sequence = list(map(int, sys.stdin.readline().split(" ")))

operators = list(map(int, sys.stdin.readline().split(" ")))

max_result = -1e9

min_result = 1e9

def cal(index, depth, cal_status):
    if index == 0:
         cal_status += sequence[depth]
    elif index == 1:
         cal_status -= sequence[depth]
    elif index == 2:
        cal_status *= sequence[depth]
    else:
        cal_status = int(cal_status / sequence[depth])

    return cal_status

def dfs(depth, operators, result):
    global max_result
    global min_result
    if depth == N:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return
    
    else:
        if operators[2] > 0:
            new_operators = [operators[0], operators[1], operators[2] - 1, operators[3]]
            dfs(depth + 1 , new_operators, cal(2, depth, result))
        if operators[3] > 0:
            new_operators = [operators[0], operators[1], operators[2], operators[3] - 1]
            dfs(depth + 1, new_operators, cal(3, depth, result))
        if operators[0] > 0:
            new_operators = [operators[0] - 1, operators[1], operators[2], operators[3]]
            dfs(depth + 1 , new_operators, cal(0, depth, result))
        if operators[1] > 0:
            new_operators = [operators[0], operators[1] - 1, operators[2], operators[3]]
            dfs(depth + 1 , new_operators, cal(1, depth, result))

dfs(1, operators, sequence[0])

print(max_result)
print(min_result)

# 주석------------
print("time : ", time.time() - start)
# ---------------