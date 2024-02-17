import math as m
def solution(a, b):
    factors = []
    
    # 기약분수화
    b //= m.gcd(a, b)
    i = 2
    # 분모의 소인수 판별
    while i <= b:
        if b % i == 0:
            factors.append(i)
            b /= i
        else: i += 1
    if (set(factors) - set([2, 5])):
        return 2
    return 1