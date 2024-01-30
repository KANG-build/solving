a = int(input())
num = sorted([int(i) for i in input().split()])
num = [i/(num[-1])*100 for i in num]
print(sum(num)/a)