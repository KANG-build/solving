from itertools import product

N, M = map(int, input().split())

for i in list(product([i+1 for i in range(N)], repeat=M)):
    for j in i:
        print(j, end=' ')
    print()