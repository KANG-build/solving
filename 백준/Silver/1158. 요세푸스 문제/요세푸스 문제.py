from collections import deque

N, K = map(int, input().split())
queue = deque([i for i in range(1, N+1)])
print('<', end='')

while len(queue) > 1:
    queue.rotate(-(K-1))
    print(queue[0], end=', ')
    queue.popleft()

print(queue[0], end='')
print('>')