import sys
import time

# 주석------------
# sys.stdin = open("/Users/jeyeolbaek/Developer/study/Algorithm/python/python.txt", "r")
# start = time.time()
# ----------------
input = sys.stdin.readline
# ----------------

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

papers = {-1: 0, 0: 0, 1: 0}


def is_uniform(x, y, size):
    first_value = matrix[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if matrix[i][j] != first_value:
                return False
    return True


def trit_tree(x, y, size):
    if is_uniform(x, y, size):
        papers[matrix[x][y]] += 1
        return

    third = size // 3

    trit_tree(x, y, third)
    trit_tree(x + third, y, third)
    trit_tree(x + 2 * third, y, third)

    trit_tree(x, y + third, third)
    trit_tree(x + third, y + third, third)
    trit_tree(x + 2 * third, y + third, third)

    trit_tree(x, y + 2 * third, third)
    trit_tree(x + third, y + 2 * third, third)
    trit_tree(x + 2 * third, y + 2 * third, third)

    return


trit_tree(0, 0, N)

print(papers[-1])
print(papers[0])
print(papers[1])

# 주석------------
# print(f"time : {time.time() - start:.5f} sec")
# ---------------
