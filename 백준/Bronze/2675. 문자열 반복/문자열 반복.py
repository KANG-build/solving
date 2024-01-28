import sys
input = sys.stdin.readline

num = int(input())
for i in range(num):
    a, b = input().split()
    print(''.join([i * int(a) for i in b]))