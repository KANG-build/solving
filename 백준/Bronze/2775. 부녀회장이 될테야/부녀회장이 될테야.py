import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())  # k층
    n = int(input())  # n호

    house = [[i for i in range(n+1)]] # 인덱스 0 빼고 1호부터 산다
    for i in range(k):
        down = house[-1]
        house += [[sum(down[:j+1]) for j in range(n+1)]]
    
    print(house[-1][-1])