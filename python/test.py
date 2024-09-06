import sys
import time

# 주석------------
sys.stdin = open('/Users/jeyeolbaek/Developer/study/Algorithm/python/python.txt', 'r')
start = time.time()
#----------------
input = sys.stdin.readline
#----------------

N = int(input())
chat_user = set()
cnt = 0
for _ in range(N):
    word = input().strip()
    
    if word == 'ENTER':
        cnt += len(chat_user)
        chat_user.clear()
    else:
        chat_user.add(word)

cnt += len(chat_user)

print(cnt)

# 주석------------
print(f"time : {time.time() - start:.5f} sec")
# ---------------