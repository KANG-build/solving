N = int(input())  # 상근이가 가지고 있는 숫자 카드의 개수
num = map(int, input().split())  # 숫자 카드에 적혀있는 정수
M = int(input())  # M개의 정수를 받겟다
IN = list(map(int, input().split()))  # 상근이가 몇개 가지고 있는지 구해야하는 정수
dic = dict(zip(IN, [0 for i in range(len(IN))]))

for i in num:
    if i in dic:
        dic[i] += 1

for i in range(M):
    print(dic[IN[i]], end=' ')