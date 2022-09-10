list_n = [10,10,10, -10,-10,-10]

count = {}
for i in list_n:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1