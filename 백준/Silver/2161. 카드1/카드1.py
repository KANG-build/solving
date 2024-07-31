from collections import deque

a = int(input())
queue = deque([i for i in range(1, a+1)])

while len(queue) > 1:
    print(queue[0], end=' ')
    queue.popleft()
    queue.rotate(-1)
    
print(queue[0])