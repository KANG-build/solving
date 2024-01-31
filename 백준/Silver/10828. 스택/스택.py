import sys
input = sys.stdin.readline

stack = []
a = int(input())
for i in range(a):
    command = input().strip()
    if command[:4] == 'push':
        stack.append(int(command[5:]))
    elif command == 'pop':
        if len(stack):
            print(stack.pop(-1))
        else: print(-1)
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        if len(stack):
            print(0)
        else: print(1)
    elif command == 'top':
        if len(stack):
            print(stack[-1])
        else: print(-1)