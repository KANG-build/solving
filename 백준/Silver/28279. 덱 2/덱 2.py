import sys
from collections import deque
input = sys.stdin.readline 

N = int(input())
stack = deque()

for i in range(N):
    a = input().rstrip()
    if a == '3':
        if stack:
            x = stack.pop()
            print(x)
        else: print(-1)
    elif a == '4':
        if stack:
            x = stack.popleft()
            print(x)
        else:print(-1)
            
    elif a == '5':
        print(len(stack))
    elif a == '6':
        if stack:
            print(0)
        else:
            print(1)
            
    elif a == '7':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif a == '8':
        if stack:
            print(stack[0])
        else:
            print(-1)
            
    else:
        n, m = map(int, a.split())
        if n == 1:
            stack.append(m)
        elif n == 2:
            stack.appendleft(m)