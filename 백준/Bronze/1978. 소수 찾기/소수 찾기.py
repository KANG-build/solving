import sys
input = sys.stdin.readline

count = 0
a = int(input())
num = map(int, input().split())
for i in num:
    for j in range(2, i):
        if i%j == 0:
            break
    else: count += 1
    if i == 1:
        count -= 1

print(count)