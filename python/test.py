import sys
# 파일 열기 모듈
# 복수 줄
sys.stdin = open("python.txt", "r")
input = sys.stdin.readline()
print(input[0].strip())
A,B = map(int, input[0].strip())
C = int(input[1])
# 한 줄
# sys.stdin = open("python.txt", "r")
# input = sys.stdin.readline()
A += C // 60
B += C % 60

if B >= 60:
    A += 1
    B -= 60
if A >= 24:
    A -= 24

print(A, B)
