from itertools import combinations_with_replacement as cwr

N, M = map(int, input().split())
num = list(map(int, input().split()))

for i in list(cwr(sorted(num), M)):
    for j in i:
        print(j, end=' ')
    print()
