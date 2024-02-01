import sys
input = sys.stdin.readline

a = int(input())
S = [0 for i in range(20)]
for idx in range(a):
    i = input().strip()
    if i[:3] == 'add':
        S[int(i[4:])-1] = 1
    elif i[:6] == 'remove':
        if S[int(i[7:])-1] == 1:
            S[int(i[7:])-1] = 0
    elif i[:5] == 'check':
        if S[int(i[6:])-1] == 1:
            print(1)
        else: print(0)
    elif i[:6] == 'toggle':
        if S[int(i[7:])-1] == 1:
            S[int(i[7:])-1] = 0
        else: S[int(i[7:])-1] = 1
    elif i == 'all':
        S = [1 for i in range(20)]
    elif i == 'empty':
        S = [0 for i in range(20)]
        