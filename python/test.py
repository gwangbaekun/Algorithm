import sys
import time

# 주석------------
sys.stdin = open('python.txt', 'r')
start = time.time()
#----------------

M = int(sys.stdin.readline())    
N = int(sys.stdin.readline())    

primeNums = []
for x in range(M, N+1):
    error = 0
    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                error += 1
                break
        if error == 0:
            primeNums.append(x)

if len(primeNums) > 0:
    print(sum(primeNums), primeNums[0], sep='\n')
else:
    print(-1)

# 주석------------
end = time.time()
print(f"{end - start:.5f} sec")
#----------------
