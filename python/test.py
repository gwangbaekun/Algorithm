import sys
import time

# 주석------------
sys.stdin = open('python.txt', 'r')
start = time.time()
#----------------

N, C = map(int, sys.stdin.readline().split(" "))
arr = [int(sys.stdin.readline()) for _ in range(N)]

arr.sort()
start = 1
end = arr[-1] - arr[0]

while start <= end:
    mid = (start + end) // 2
    cur = arr[0]
    count = 1

    for i in range(1, len(arr)):
        if arr[i] >= cur + mid:
            count += 1
            cur = arr[i]

    if count >= C:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)

# 주석------------
print(f"time : {time.time() - start:.5f} sec")
# ---------------