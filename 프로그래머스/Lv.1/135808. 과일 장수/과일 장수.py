def solution(k, m, score):
    apple = sorted(score, reverse=True)
    appleBox = [apple[i:i+m] for i in range(0, len(apple), m)]
    return sum(min(i) * m for i in appleBox if len(i) == m)