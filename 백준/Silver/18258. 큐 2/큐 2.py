import sys
from collections import deque 
input = sys.stdin.readline

N = int(input())
queue = deque()

for i in range(N):
    command = input().strip()
    if command == 'pop':
        if len(queue) == 0:
            print(-1)
        else: 
            print(queue[0])
            queue.popleft()
    elif command == 'size':
        print(len(queue))
    elif command == 'front':
        if len(queue) == 0:
            print(-1)
        else: print(queue[0])
    elif command == 'back':
        if len(queue) == 0:
            print(-1)
        else: print(queue[-1])
    elif command == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    else:
        push, num = command.split()
        queue.append(int(num))