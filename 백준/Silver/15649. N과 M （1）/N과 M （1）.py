import sys
from itertools import permutations
input = sys.stdin.readline 

N, M = map(int, input().split())

for i in list(permutations([i+1 for i in range(N)], M)):
    for j in i:
        print(j, end=' ')
    print()
