from itertools import combinations

while True:
    a = list(map(int, input().split()))
    if a == [0]:
        break
    for i in list(combinations(a[1:], 6)):
        for j in i:
            print(j, end=' ')
        print()
    print()