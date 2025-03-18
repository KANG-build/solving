import math

def solution(progresses, speeds):
    answer_list = []
    for i in range(len(progresses)):
        answer_list.append(math.ceil((100-progresses[i])/speeds[i]))
        
    answer = [1]
    day = 0
    for i in range(1, len(answer_list)):
        # 전꺼보다 크면 새거에서 시작
        day = max(day, answer_list[i-1])
        if answer_list[i] > day:
            answer.append(1)
        else:
            answer[-1] += 1
    return answer