def solution(n):
    return sum([j for j in range(1, n+1) if n % j == 0])