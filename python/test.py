import sys

# sys.stdin = open("python.txt", "r")

N, M = sys.stdin.readline().split()

def opposite(num):
    return int(num[0]) + int(num[1]) * 10 + int(num[2]) * 100

if opposite(N) > opposite(M):
    print(opposite(N))
else:
    print(opposite(M))
