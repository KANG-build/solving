from itertools import combinations

N, M = map(int, input().split())
num = list(map(int, input().split()))
answer = []

for i in list(combinations(sorted(num), M)):
    new = []
    for j in i:
        new.append(j)
    if new not in answer:
        for a in new:
            print(a, end=' ')
        print()
    answer.append(new)
