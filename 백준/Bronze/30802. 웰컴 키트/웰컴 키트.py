import math

N = int(input())
size = map(int, input().split())
T, P = map(int, input().split())
sum = 0

for i in size:
    sum += math.ceil(i/T)
    
print(sum)
print(N//P, N-(N//P)*P)
