import sys
input = sys.stdin.readline

a = map(int, input().split())
chess = [1, 1, 2, 2, 2, 8]
for i, j in zip(a, chess):
    print(j-i, end=' ')