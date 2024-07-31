import sys
from itertools import permutations
input = sys.stdin.readline

a = int(input())
for i in list(permutations([i+1 for i in range(a)], a)):
    for j in i:
        print(j, end=' ')
    print()
