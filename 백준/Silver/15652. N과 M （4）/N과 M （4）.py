from itertools import combinations_with_replacement as cwr

N, M = map(int, input().split())

for i in list(cwr([i+1 for i in range(N)], M)):
    for j in i:
        print(j, end=' ')
    print()