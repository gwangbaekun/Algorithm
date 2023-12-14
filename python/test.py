import sys
import time
from collections import deque

# 주석------------
sys.stdin = open('/Users/home/Developer/study/Algorithm/python/python.txt', 'r')
start = time.time()
#----------------

class Queue:
    def __init__(self):
        """Initialize an empty queue."""
        self._queue = deque()

    def push(self, data):
        """Add an element to the back of the queue."""
        self._queue.append(data)

    def pop(self):
        """Remove and return the front element of the queue."""
        return self._queue.popleft() if self._queue else -1

    def size(self):
        """Return the number of elements in the queue."""
        return len(self._queue)

    def empty(self):
        """Check if the queue is empty."""
        return not self._queue
    
    def is_empty(self):
         if self.empty():
             return 1
         else:
             return 0

    def front(self):
        """Return the front element of the queue without removing it."""
        return self._queue[0] if not self.empty() else -1

    def back(self):
        """Return the back element of the queue without removing it."""
        return self._queue[-1] if not self.empty() else -1
        
queue = Queue()

N = int(sys.stdin.readline())

for _ in range(N):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'push':
        queue.push(int(cmd[1]))
    elif cmd[0] == 'pop':
        print(queue.pop())
    elif cmd[0] == 'size':
        print(queue.size())
    elif cmd[0] == 'empty':
        print(queue.is_empty())
    elif cmd[0] == 'front':
        print(queue.front())
    elif cmd[0] == 'back':
        print(queue.back())

# 주석------------
print(f"time : {time.time() - start:.5f} sec")
# ---------------
