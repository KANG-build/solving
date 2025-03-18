from collections import deque

def solution(priorities, location):
    queue = deque(priorities)
    answer = 0
    while True:
        # 내 차례가 왔을 때 
        if location == 0:
            if queue[0] == max(queue):
                answer += 1
                return answer
            else:
                queue.rotate(-1)
                location = len(queue)-1
        # 일반
        else:
            # 앞이 제일 작을 때
            if queue[0] == max(queue):
                queue.popleft()
                answer += 1
            else:
                queue.rotate(-1)
            location -= 1
    
    return priorities, location