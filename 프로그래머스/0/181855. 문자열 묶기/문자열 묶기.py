def solution(strArr):
    a = {}
    for i in strArr:
        if len(i) in a:
            a[len(i)] += 1
        else: a[len(i)] = 1
    return max(a.values())