def solution(n):
    return next(i for i in range(1, n) if n % i == 1)
