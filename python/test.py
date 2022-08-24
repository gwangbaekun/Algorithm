import time
import sys

# 주석------------
# sys.stdin = open('python.txt', 'r')
# start = time.time()
#----------------

N = int(sys.stdin.readline())

words = [sys.stdin.readline().strip() for _ in range(N)]

new_words_list = []
length_sort = []

for i in words:
    new_obj = {
        'word': i,
        'length': len(i)
    }
    new_words_list.append(new_obj)
    length_sort.append(len(i))


length_sort.sort()

real_sorted_length_array = []

for i in range(len(length_sort)):
    if length_sort[i] in real_sorted_length_array:
        pass
    else:
        real_sorted_length_array.append(length_sort[i])

answer = []

for i in real_sorted_length_array:
    to_sort = []
    for j in new_words_list:
        if i == j['length']:
            to_sort.append(j)

    # work with sort
    to_sort.sort(key=lambda x: x['word'])
    for j in to_sort:
        answer.append(j['word'])

# print(answer)

new_answer = []

for i in answer:
    if i in new_answer:
        pass
    else:
        new_answer.append(i)

for i in new_answer:
    print(i)




# 주석------------
# print("time : ", time.time() - start)
#----------------