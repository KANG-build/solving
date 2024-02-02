import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    s = input().strip()
    print(s[0], end='')
    print(s[-1])