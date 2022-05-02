import test
import sys
sys.stdin = open("python.txt", "r")
input = sys.stdin.readline

def cont():
    while(True):
        try:
            problem.main0()
        except Exception as e:
            print("exception =", e)
            return

if _name_ == "__main__":
    problem.main(0)()
    cont()