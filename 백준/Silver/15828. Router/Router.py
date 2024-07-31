import sys
from collections import deque 
input = sys.stdin.readline

a = int(input())
queue = deque(maxlen=a)

while True:
    command = int(input())
    if command == -1:
        break
    elif command == 0:
        queue.popleft()
    else:
        queue.append(command)
        
for i in queue:
    print(i, end=' ')