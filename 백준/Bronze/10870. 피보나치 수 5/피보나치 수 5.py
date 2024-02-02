import sys
input = sys.stdin.readline

n = int(input())
a = 0
b = 1
c = a+b

for i in range(n):
    a = b
    b = c
    c = a+b
    
print(a)