import sys
import time

# 주석------------
# sys.stdin = open("/Users/jeyeolbaek/Developer/study/Algorithm/python/python.txt", "r")
# start = time.time()
# ----------------
input = sys.stdin.readline
# ----------------

expression = input()

subtraction_groups = expression.split("-")

total = sum(map(int, subtraction_groups[0].split("+")))


for group in subtraction_groups[1:]:
    total -= sum(map(int, group.split("+")))

print(total)


# 주석------------
# print(f"time : {time.time() - start:.5f} sec")
# ---------------
