def solution(array, n):
    return sorted([(abs(i-n), i) for i in array])[0][1]