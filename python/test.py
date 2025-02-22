import sys
import time

# 주석------------
# sys.stdin = open("/Users/jeyeolbaek/Developer/study/Algorithm/python/python.txt", "r")
# start = time.time()
# ----------------
input = sys.stdin.readline
# ----------------

N = int(input())
l = [list(input().strip()) for _ in range(N)]


def all_same(iterable):
    first_value = iterable[0]

    return (
        first_value
        if all(x == first_value for x in iterable)
        else f"({"".join(iterable)})"
    )


def zip_with_2(list, depth):
    if depth == 1:
        return list[0][0]

    zipped_list = []

    for i in range(0, depth, 2):
        zip_string = []
        for j in range(0, depth, 2):
            _iterable = [list[i][j], list[i][j + 1], list[i + 1][j], list[i + 1][j + 1]]
            zip_string.append(all_same(_iterable))
        zipped_list.append(zip_string)

    return zip_with_2(zipped_list, int(depth / 2))


if N == 1:
    print(l[0][0])
else:
    result = zip_with_2(l, N)
    print(result)

# 주석------------
# print(f"time : {time.time() - start:.5f} sec")
# ---------------
