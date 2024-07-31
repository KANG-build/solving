import sys
import math
input = sys.stdin.readline

numer1, denom1 = map(int, input().split())
numer2, denom2 = map(int, input().split())

a = numer1*denom2 + numer2*denom1
b = denom1*denom2
gcd = math.gcd(a, b)

print(a//gcd, b//gcd)