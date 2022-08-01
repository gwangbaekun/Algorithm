import sys
import time

# 주석------------
sys.stdin = open('python.txt', 'r')
start = time.time()
#----------------

Num = sys.stdin.readline()

def block_reculsive(N):
    if (N == 1):
        track = [[1, 3]]
        return track

    track = block_reculsive(N - 1)

    if (N % 2 == 1):
        track.append([3,2])
        track.append([1,2])
        track.append([1,3])
        return track

    
    if (N % 2 == 0):
        track.append([2,3])
        track.append([2,1])
        track.append([1,3])
        return track

for block in block_reculsive(Num):
    print(block)



# 주석------------
end = time.time()
print(f"{end - start:.5f} sec")
#----------------
