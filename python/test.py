import sys
import time

# 주석------------
# sys.stdin = open('python.txt', 'r')
# start = time.time()
#----------------

N, M = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

# combination
def combination(arr, num):
    result = []
    if num == 0:
        return [[]]

    for i in range(len(arr)):
        elem = arr[i]
        for rest in combination(arr[i + 1:], num - 1):
            result.append([elem] + rest)
    return result

blackjack_sum = []

# find sum
for i in combination(cards, 3):
    combination_sum = 0
    for j in i:
        combination_sum = combination_sum + j
    blackjack_sum.append(combination_sum)

answer = 0
# find smallest
for i in blackjack_sum:
    contrast = M - i
    if (contrast >= 0 and contrast < M - answer):
        answer = i

print(answer)

# 주석------------
# end = time.time()
# print(f"{end - start:.5f} sec")
#----------------
