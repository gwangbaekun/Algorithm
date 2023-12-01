import sys
import time

# 주석------------
sys.stdin = open('/Users/home/Developer/study/Algorithm/python/python.txt', 'r')
start = time.time()
#----------------

N = int(sys.stdin.readline())
members = dict()
for _ in range(N):
    name, status = sys.stdin.readline().split()
    if status == 'enter':
        members[name] = status
    else:
        members.pop(name)
        
members = sorted(members.keys(), reverse=True)

for member in members:
    print(member)

# 주석------------
print(f"time : {time.time() - start:.5f} sec")
# ---------------
