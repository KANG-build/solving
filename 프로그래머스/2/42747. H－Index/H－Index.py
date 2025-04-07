def solution(citations):
    answer = 0
    
    # 풀기
    citations_list = [0] * (max(citations)+1)
    for h in sorted(citations, reverse=True):
        for i in range(h+1):
            citations_list[i] += 1    
    
    # 세기
    for idx, h in enumerate(citations_list):
        # idx+1 >= h -> h번 이상 인용된 논문이 h편 이상 
        # 어차피 남은 논문이 h보다 작음
        if idx >= h:
            answer = h
            break
    
    return answer