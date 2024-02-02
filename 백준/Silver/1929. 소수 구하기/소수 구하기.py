import sys
input = sys.stdin.readline

a, b = map(int, input().split())
for n in range(max(2, a), b+1):
    for i in range(2, int(n**0.5+1)):
        if n%i == 0:
            break
    else: print(n)