# 제곱근 소수 구하기
def primenum(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

# 에라토스테네스 체
def primeList(n):
    n += 1
    sieve = [False, False] + [True] * (n)
    end = int(n ** 0.5) + 1
    for i in range(2, end):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False
    return [i for i in range(n) if sieve[i] == True]