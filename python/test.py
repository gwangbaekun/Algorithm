import sys
import time

# 주석------------
# sys.stdin = open('/Users/home/Developer/study/Algorithm/python/python.txt', 'r')
# start = time.time()
#----------------

N = int(sys.stdin.readline())

class stack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, num):
        self.stack.append(num)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return -1
        else:
            self.size -= 1
            return self.stack.pop()
    
    def size(self):
        return self.size

    def empty(self):
        if self.size == 0:
            return 1
        else:
            return 0
    
    def top(self):
        if self.size == 0:
            return -1
        else:
            return self.stack[-1]
        
stack = stack()

for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == '1':
        stack.push(int(command[1]))
    elif command[0] == '2':
        print(stack.pop())
    elif command[0] == '3':
        print(stack.size)
    elif command[0] == '4':
        print(stack.empty())
    elif command[0] == '5':
        print(stack.top())

# 주석------------
# print(f"time : {time.time() - start:.5f} sec")
# ---------------
