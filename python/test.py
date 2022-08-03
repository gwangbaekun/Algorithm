import sys
import time

# 주석------------
sys.stdin = open('python.txt', 'r')
start = time.time()
#----------------

N = int(sys.stdin.readline())

result = 0

for i in range(1, N+1):
    A = list(map(int, str(i)))
    result = i + sum(A)

    if (result == N):
        print(i)
        break

    if i == N:
        print(0)


# 주석------------
end = time.time()
print(f"{end - start:.5f} sec")
#----------------
