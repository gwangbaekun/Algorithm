def one_two_three(n):
    # just do it!
    if n == 0:
        return [0, 0]
    else:
        return [int(str('9' * (n // 9)) + str(n % 9)) , int('1' * n)] if n % 9 != 0 else [int(str('9' * (n // 9))) , int('1' * n)]
        