import sys
input = sys.stdin.readline

A, B, C, D = map(str, input().split())
print(int(A+B)+int(C+D))