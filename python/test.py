import sys
import time

# 주석------------
sys.stdin = open('/Users/home/Developer/study/Algorithm/python/python.txt', 'r')
start = time.time()
#----------------

N, M = map(int, sys.stdin.readline().split())
board = [sys.stdin.readline().rstrip() for _ in range(N)]

bf_ans = 0

result = []

def check(i, j, board):
    w_cnt = 0
    b_cnt = 0
    for x in range(i, i + 8):
        for y in range(j, j + 8):
            # w 로 시작했을 때
            if (x + y) % 2 == 0:
                if board[x][y] != 'W':
                    w_cnt += 1
            else:
                if board[x][y] != 'B':
                    w_cnt += 1

            if (x + y) % 2 == 0:
                if board[x][y] != 'B':
                    b_cnt += 1
            else:
                if board[x][y] != 'W':
                    b_cnt += 1

    return min(w_cnt, b_cnt)

#시작을 찾기
for i in range(N - 7):
    for j in range(M - 7):
        ans = check(i, j, board)
        if bf_ans == 0 or ans < bf_ans:
            bf_ans = ans
        result.append(check(i, j, board))
        

print(min(result), bf_ans)

# 주석------------
print(f"time : {time.time() - start:.5f} sec")
# ---------------

