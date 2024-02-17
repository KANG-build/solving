import math as m
def solution(a, b):

    b //= m.gcd(a, b)
    
    while b%2 == 0:
        b //= 2
    while b%5 == 0:
        b //= 5
    if b == 1:
        return 1
    return 2