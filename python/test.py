import sys
import time

# 주석------------
# sys.stdin = open('/Users/home/Developer/study/Algorithm/python/python.txt', 'r')
# start = time.time()
#----------------

def checkClose(stack):
    if len(stack) == 0 or len(stack) == 1:
        return stack
    if stack[len(stack) - 1] == ')' and stack[len(stack) - 2] == '(':
        stack.pop()
        stack.pop()
    elif stack[len(stack) - 1] == ']' and stack[len(stack) - 2] == '[':
        stack.pop()
        stack.pop()
    return stack

while True:
    try:
        testString = sys.stdin.readline().rstrip()

        if (testString == '.'):
            break

        if (testString[len(testString) - 1] == '.'):
            stack = []
            for i in range(len(testString) - 1):
                if (testString[i] == '(' or testString[i] == '[' or testString[i] == ')' or testString[i] == ']'): 
                    stack.append(testString[i])
                    stack = checkClose(stack)
            if len(stack) == 0:
                print('yes')
            else:
                print('no')
    except:
        break

# 주석------------
# print(f"time : {time.time() - start:.5f} sec")
# ---------------
