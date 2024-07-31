from itertools import combinations_with_replacement as cwr

N, M = map(int, input().split())
num = list(map(int, input().split()))
answer = []

for i in list(cwr(sorted(num), M)):
    new = []
    for j in i:
        new.append(j)
    if new not in answer:
        for a in new:
            print(a, end=' ')
        print()
    answer.append(new)