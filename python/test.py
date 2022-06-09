import sys

# sys.stdin = open("python.txt", "r")

A, B, C = map(int, sys.stdin.readline().strip().split())
count = 0
if B >= C:
    print(-1)
else:
    print(A // (C - B) + 1)