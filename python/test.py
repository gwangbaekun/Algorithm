import sys
import time

# sys.stdin = open("python.txt", "r")
start = time.time()
N = int(sys.stdin.readline())

if N % 5 == 0:
    print(N // 5)
else:
    p = 0
    while N > 0:
        N -= 3
        p += 1
        if N % 5 == 0:
            p += N // 5
            print(p)
            break
        elif N == 1 or N == 2:
            print(-1)
            break
        elif N == 0:
            print(p)
            break

end = time.time()

# print(f'{end-start:.5f} sec')