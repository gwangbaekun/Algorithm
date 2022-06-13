import sys
import time

# sys.stdin = open("python.txt", "r")
start = time.time()
N = int(sys.stdin.readline())

for _ in range(N):
    H, W, G = map(int, sys.stdin.readline().split())
    height = G % H # 4층
    number = G // H + 1
    if height == 0:
        height = H
        number = G // H
    if number < 10:
        print(str(height) + "0" + str(number))
    else:
        print(str(height) + str(number))

end = time.time()

# print(f'{end-start:.5f} sec')