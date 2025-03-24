def solution(arr):
    for idx, i in enumerate(arr):
        if i >= 50 and i%2 == 0:
            i /= 2
        elif i < 50 and i%2 == 1:
            i = 2*i + 1
    return i