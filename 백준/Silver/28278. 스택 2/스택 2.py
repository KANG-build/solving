import sys
input = sys.stdin.readline

N = int(input().rstrip())
stack = []

for i in range(N):
    a = input().rstrip()
    if a == '2':
        if stack:
            x = stack.pop()
            print(x)
        else: print(-1)
    elif a == '3':
        print(len(stack))
    elif a == '4':
        if stack:
            print(0)
        else:
            print(1)
    elif a == '5':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    else:
        n, m = map(int, a.split())
        stack.append(m)