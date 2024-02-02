import sys
import math
input = sys.stdin.readline

a = int(input())
for i in range(a):
    A, B = map(int, input().split())
    print(A*B//math.gcd(A, B))