import sys
import time

# 주석------------
# sys.stdin = open("/Users/jeyeolbaek/Developer/study/Algorithm/python/python.txt", "r")
# start = time.time()
# ----------------
input = sys.stdin.readline
# ----------------

N = int(input())
dis = list(map(int, input().split(" ")))
gases = list(map(int, input().split(" ")))

min_price = gases[0]
sum_gas_price = 0

for i in range(N - 1):
    min_price = min(gases[i], min_price)
    sum_gas_price += min_price * dis[i]

print(sum_gas_price)

# 주석------------
# print(f"time : {time.time() - start:.5f} sec")
# ---------------
