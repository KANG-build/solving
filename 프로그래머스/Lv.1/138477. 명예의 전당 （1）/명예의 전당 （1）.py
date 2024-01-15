def solution(k, score):
    명예의전당 = []
    answer = []
    # score 삽입
    for i in score:
        명예의전당.append(i)
    # 범위 넘어가면 뺀다
        if len(명예의전당) > k:
            명예의전당.remove(min(명예의전당))
    # 제일 작은 수를 추가한다
        answer.append(min(명예의전당))
    return answer