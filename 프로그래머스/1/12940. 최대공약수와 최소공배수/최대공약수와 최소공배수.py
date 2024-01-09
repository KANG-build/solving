def solution(n, m):
    # 유클리드 호제법
    c, d = max(n, m), min(n, m)
    t = 1
    while(t):
        t = c%d
        c, d = d, t
    # 두 자연수의 곱 = 최대공약수 x 최소공배수
    return [c, n*m//c]