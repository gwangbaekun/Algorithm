import time
import sys

# 주석------------
sys.stdin = open('python.txt', 'r')
start = time.time()
#----------------


n = int(input())

word = []
for i in range(n):
    word.append(input())

set_word = list(set(word))

sort_word = []

for i in set_word:
    sort_word.append((len(i), i))

result = sorted(sort_word)

print(result)

# 주석------------
print("time : ", time.time() - start)
#----------------