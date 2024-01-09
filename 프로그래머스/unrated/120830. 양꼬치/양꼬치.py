def solution(n, k):
    a = n // 10
    answer = n*12000 + (k-a)*2000
    return answer