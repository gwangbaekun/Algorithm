import sys
import time
# 주석------------
sys.stdin = open('python.txt', 'r')
start = time.time()
#----------------

N = int(sys.stdin.readline())
d = []
for _ in range(6):
    a, b = map(int, sys.stdin.readline().split(" "))
    d.append([a, b])

max_a = 0
max_a_index = -1

for i in range(6):
    if d[i][1] > max_a:
        max_a = d[i][1]
        max_a_index = i

side = None

if d[(max_a_index + 1) % 6][1] > d[max_a_index - 1][1]:
    side = d[(max_a_index + 1) % 6][1]
    empty_a = d[max_a_index - 2][1]
    empty_b = d[max_a_index - 3][1]
    print(N * (side * max_a - empty_a * empty_b))
else:
    side = d[max_a_index - 1][1]
    empty_a = d[(max_a_index + 2) % 6][1]
    empty_b = d[(max_a_index + 3) % 6][1]
    print(N * (side * max_a - empty_a * empty_b))



# 주석------------
print("time : ", time.time() - start)
#----------------