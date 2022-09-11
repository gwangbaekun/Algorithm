# combination
def combination(arr, num):
    result = []
    if num == 0:
        return [[]]

    for i in range(len(arr)):
        elem = arr[i]
        for rest in combination(arr[i + 1:], num - 1):
            result.append([elem] + rest)
    return result
