import math


a = int(input())
for i in range(a):
    m, n = map(int, input().split())
    print(math.factorial(n)//(math.factorial(m)*math.factorial(abs(m-n))))