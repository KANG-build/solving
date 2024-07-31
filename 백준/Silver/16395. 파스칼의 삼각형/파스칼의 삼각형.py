import math
n, m = map(int, input().split())
n -= 1
m -= 1

print(math.factorial(n)//(math.factorial(m)*math.factorial(abs(m-n))))