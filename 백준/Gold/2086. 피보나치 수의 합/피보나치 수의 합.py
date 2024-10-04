import sys
sys.setrecursionlimit(100000000)

a, b = map(int, input().split())

# 두 개의 수를 구한다
memo = {0:0, 1:1, 2:1}
def fibo(n):
    if n not in memo:
        if n%2: # 홀수
            a = fibo(n//2)
            b = fibo(n//2+1)
            memo[n] = (a**2 + b**2)%1000000000
        else:  # 짝수
            a = fibo(n//2)
            b = fibo(n//2-1)
            memo[n] = (a * (a + 2*b))%1000000000
    return memo[n]

print((fibo(b+2)-fibo(a+1))%1000000000)
