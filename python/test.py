import sys

# sys.stdin = open("python.txt", "r")

word = sys.stdin.readline().strip()

upWord = word.upper()
wordSet = list(set(upWord))

countlist = []
for char in wordSet:
    count = 0
    for i in upWord:
        if char == i:
            count += 1
    countlist.append(count)

def max_num(list):
    arr = []
    for i in range(len(list)):
        if list[i] == max(list):
            arr.append(i)
    if len(arr) == 1:
        return arr[0]
    else:
        return "?"

if max_num(countlist) == '?':
    print("?")
else:
    print(wordSet[max_num(countlist)])