from itertools import combinations

N, M = map(int, input().split())
num = list(map(int, input().split()))

for i in list(combinations(sorted(num), M)):
    for j in i:
        print(j, end=' ')
    print()
