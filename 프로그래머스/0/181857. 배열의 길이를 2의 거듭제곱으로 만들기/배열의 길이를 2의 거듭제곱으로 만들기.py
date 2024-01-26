def solution(arr):
    n = 0
    while 2**n < len(arr):
        n += 1
    return arr + [0 for i in range(2**n - len(arr))]