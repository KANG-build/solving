import math as m

a, b = map(int, input().split())
print(m.gcd(a, b))
print(a*b//m.gcd(a,b))