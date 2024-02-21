import sys
input = sys.stdin.readline

count = 0
a, money = map(int, input().split())
coin = []
for i in range(a):
  b = int(input())
  coin.append(b)

for i in coin[::-1]:
  if money//i:
    count += money//i
    money %= i
    
print(count)