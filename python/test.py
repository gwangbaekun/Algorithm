import sys
import time
# 주석------------
sys.stdin = open('python.txt', 'r')
start = time.time()
#----------------

while True:
    a, b, c = map(int, sys.stdin.readline().split(" "))
    heru = max(a, b, c)
    ausar = min(a, b, c) 
    auset = (a+b+c) - heru - ausar
    if a == 0 and b == 0 and c == 0:
        break
    if ausar ** 2 + auset ** 2 == heru ** 2:
        print("right")
    else:
        print("wrong")

# 주석------------
print("time : ", time.time() - start)
#----------------