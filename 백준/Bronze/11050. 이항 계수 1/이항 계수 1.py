n, k = map(int, input().split())
N = 1
K = 1
NK = 1
for i in range(1, n+1):
    N *= i
for i in range(1, k+1):
    K *= i
for i in range(1, n-k+1):
    NK *= i

print(N//(K*NK))