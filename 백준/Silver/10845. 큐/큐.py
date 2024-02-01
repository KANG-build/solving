import sys
input = sys.stdin.readline

a = int(input())
queue = []
for i in range(a):
    s = input().strip()
    
    if s[:4] == 'push':
        queue.append(int(s[5:]))
    elif s == 'empty':
        if len(queue):
            print(0)
        else: print(1)
    elif s == 'size':
        print(len(queue))
    elif s == 'front':
        if len(queue):
            print(queue[0])
        else: print(-1)
    elif s == 'back':
        if len(queue):
            print(queue[-1])
        else: print(-1)
    elif s == 'pop':
        if len(queue):
            print(queue.pop(0))
        else: print(-1)