
from collections import deque 
a = int(input())

for i in range(a):
    answer = 1
    N, M = map(int, input().split())  # 문서의 개수, 몇번째
    queue = deque(list(map(int, input().split())))
    
    # 내꺼가 최상이 아니면 rotate
    # 중요도대로 큰거부터 인쇄
    while len(queue) > 0:
  
        if max(queue) <= queue[0]:
            if M == 0:
                print(answer)
                break
            queue.popleft()
            answer += 1
        else: queue.rotate(-1)
        if M == 0:
            M = len(queue)
        M -= 1