import sys

# sys.stdin = open("python.txt", "r")
input = sys.stdin.readline()
A,B,C = map(int, input.strip().split())

if (A == B == C):
    print(10000 + A * 1000)
elif (A == B):
    print(1000 + A * 100)
elif (B == C):
    print(1000 + B * 100)
elif (C == A):
    print(1000 + C * 100)
else:
    print(100 * max(A,B,C))
    


# sys.stdin.close()

