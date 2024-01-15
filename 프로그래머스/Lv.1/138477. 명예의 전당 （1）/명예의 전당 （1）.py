def solution(k, score):
    명예의전당 = []
    answer = []
    # score 삽입
    for i in score:
        명예의전당.append(i)
    # 작은 순으로 정렬
        명예의전당 = sorted(명예의전당)
    # 범위 넘어가면 뺀다
        if len(명예의전당) > k:
            명예의전당.pop(0)
    # 제일 작은 수를 추가한다
        answer.append(명예의전당[0])
    return answer