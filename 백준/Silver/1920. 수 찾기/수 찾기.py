import sys
input = sys.stdin.readline

temp1 = int(input())
num1 = set(map(int, input().split()))
temp2 = int(input())
num2 = list(map(int, input().split()))

for i in num2:
    if i in num1:
        print(1)
    else: print(0)