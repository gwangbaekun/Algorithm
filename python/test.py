import sys
import time
import copy

# 주석------------
# sys.stdin = open('python.txt', 'r')
# start = time.time()
#----------------

input_row = []
            
for _ in range(9):
    input_row.append(list(map(int, sys.stdin.readline().split(" "))))

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)

def is_valid(board, num, pos):

    for i in range(len(board)):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[0] // 3
    box_y = pos[1] // 3

    for i in range(box_x * 3, box_x * 3 + 3):
        for j in range(box_y * 3, box_y * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def sudoku(board):
    empty = find_empty(board)
    if not empty:
        return True
    else:
        row, col = empty

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if sudoku(board):
                return True
            
            board[row][col] = 0

    return False


sudoku(input_row)

for elem in input_row:
    print(" ".join(map(str, elem)))

# 주석------------
# print("time : ", time.time() - start)
# ---------------