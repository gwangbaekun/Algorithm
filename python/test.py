import sys

# sys.stdin = open("python.txt", "r")

N = int(sys.stdin.readline().strip())

arr = list(sys.stdin.readline().strip() for _ in range(N))

count = 0
for word in arr:
    chars = []
    for i in word:
        if i in chars and chars[-1] is not i:
            count += -1
            break
        else:
            chars.append(i)
    count += 1

print(count)