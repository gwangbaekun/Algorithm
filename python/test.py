import sys
import time

# 주석------------
sys.stdin = open('/Users/home/Developer/study/Algorithm/python/python.txt', 'r')
start = time.time()
#----------------

gradeTransformer = {
   'A+': 4.5,
   'A0': 4.0,
   'B+': 3.5,
   'B0': 3.0,
   'C+': 2.5,
   'C0': 2.0,
   'D+': 1.5,
   'D0': 1.0,
   'F': 0,
   'P': 0
}

grades = 0
scores = 0

for _ in range(20):
    _, grade, score = sys.stdin.readline().strip().split(" ")
    if score != 'P': 
        grades += float(grade)
        scores += gradeTransformer[score] * float(grade)

print('%.6f' % (scores / grades))

# 주석------------
print(f"time : {time.time() - start:.5f} sec")
# ---------------

