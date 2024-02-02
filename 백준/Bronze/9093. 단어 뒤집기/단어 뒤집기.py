import sys
input = sys.stdin.readline

num = int(input())
for i in range(num):
    s = input().strip().split(' ')
    for i in s:
        print(i[::-1], end=' ')