
a = int(input())
for i in range(a):
    memo = [[1, 0], [0, 1]]
    n = int(input())

    for index in range(2, n+1):
        memo.append([memo[index-1][0] + memo[index-2][0], memo[index-1][1] + memo[index-2][1]])

    for j in memo[n]:
        print(j, end=' ')
    print()