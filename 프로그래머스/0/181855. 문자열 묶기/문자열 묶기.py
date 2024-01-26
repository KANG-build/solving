def solution(strArr):
    a = [0] * 31
    for i in strArr:
        a[len(i)] += 1
    return max(a)