import sys
input = sys.stdin.readline

a = int(input())
num = list(map(int, input().split()))
num = sorted(num)
SUM = 0
for idx, n in enumerate(num):
    SUM += sum(num[:idx+1])
print(SUM)