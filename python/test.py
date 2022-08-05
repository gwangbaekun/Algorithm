import sys
import time

# 주석------------
sys.stdin = open('python.txt', 'r')
# start = time.time()
#----------------

N, M = map(int ,sys.stdin.readline().split())
A = [sys.stdin.readline().strip() for _ in range(M)]

b_row = 'BWBWBWBW'
w_row = 'WBWBWBWB'

# 시작점을 골라서
_result = []
for i in range(N - 8 + 1):
    for j in range(M - 8 + 1):
        _result.append([i, j])

result = []
# 체스판 만들기
for start in _result:
    chessBoard = []
    count = 0
    B = A[start[0]:start[0] + 8]
    for chess in B:
        chessBoard.append(chess[start[1]: start[1] + 8])

    which_is_smaller = []
    # 정상 체스보드와 비교
    for i in range(8):
        for j in range(8):
            if (i % 2 == 0):
                if (b_row[j] != chessBoard[i][j]):
                    count += 1
            else:
                if (w_row[j] != chessBoard[i][j]):
                    count += 1
    which_is_smaller.append(count)
    count = 0
    for i in range(8):
        for j in range(8):
            if (i % 2 == 0):
                if (w_row[j] != chessBoard[i][j]):
                    count += 1
            else:
                if (b_row[j] != chessBoard[i][j]):
                    count += 1
    which_is_smaller.append(count)
    result.append(min(which_is_smaller))

print(min(result))

# 주석------------
# end = time.time()
# print(f"{end - start:.5f} sec")
#----------------
