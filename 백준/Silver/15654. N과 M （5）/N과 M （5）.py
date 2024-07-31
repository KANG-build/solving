from itertools import permutations

N, M = map(int, input().split())
num = list(map(int, input().split()))

for i in sorted(list(permutations(num, M))):
    for j in i:
        print(j, end=' ')
    print()
