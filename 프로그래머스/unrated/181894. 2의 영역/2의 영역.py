def solution(arr):
    if 2 in arr:
        a = arr.index(2)
        b = arr[::-1].index(2)
        if b == 0:
            return arr[a:]
        return arr[a:-b]
    return [-1]