import sys
import time
from math import gcd
# 주석------------
# sys.stdin = open('python.txt', 'r')
# start = time.time()
#----------------

N = int(sys.stdin.readline())

board = list(map(int, sys.stdin.readline().split(" ")))

for i in range(1, N):
    to_gcd = gcd(board[0], board[i])
    print(str(board[0]//to_gcd) + "/" + str(board[i]//to_gcd))
    
# 주석------------
# print("time : ", time.time() - start)
# ----------------