import sys

# sys.stdin = open("python.txt", "r")

N = int(sys.stdin.readline())

room = 1
count = 1
while True:
    if (N <= room):
        print(count)
        break
    room += count * 6
    count += 1
