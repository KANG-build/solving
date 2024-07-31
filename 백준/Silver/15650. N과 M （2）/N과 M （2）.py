from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

for i in list(combinations([i+1 for i in range(N)], M)):
    for j in i:
        print(j, end=' ')
    print()