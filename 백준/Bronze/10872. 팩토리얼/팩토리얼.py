import sys
input = sys.stdin.readline

a = int(input())
n = 1
for i in range(1, a+1):
    n *= i
print(n)