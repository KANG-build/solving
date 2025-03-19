def solution(a, b):
    answer = 0
    M = max(a, b)
    m = min(a, b)
    for i in range(m, M+1):
        answer += i
    return answer