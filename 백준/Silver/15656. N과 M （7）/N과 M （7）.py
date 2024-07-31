from itertools import product

N, M = map(int, input().split())
num = list(map(int, input().split()))

for i in list(product(sorted(num), repeat=M)):
    for j in i:
        print(j, end=' ')
    print()
