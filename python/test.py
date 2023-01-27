import sys
import time

# 주석------------
sys.stdin = open('python.txt', 'r')
start = time.time()
#----------------

N = int(sys.stdin.readline())

for _ in range(N):
    test = sys.stdin.readline().strip()
    left = 0
    right = 0
    for elem in test:
        if elem == '(':
            left += 1
        else:
            right += 1
        
        if right > left:
            break
    
    if right == left:
        print('YES')
    else:
        print('NO')
    
    

# 주석------------
print(f"time : {time.time() - start:.5f} sec")
# ---------------