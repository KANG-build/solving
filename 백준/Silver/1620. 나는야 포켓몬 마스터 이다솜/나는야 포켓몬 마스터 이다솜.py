import sys
input = sys.stdin.readline

N, M = map(int, input().split())
poket = {}
for i in range(N):
    poketmon = input().strip()
    poket[poketmon] = i+1
tekop = {str(v):k for k, v in poket.items()}  
for j in range(M):
    Q = input().strip()
    if Q.isdigit():
        print(tekop[Q])
    else:
        print(poket[Q])