def solution(citations):
    answer = 0
    
    for idx, h in enumerate(sorted(citations, reverse=True)):
        # idx+1 >= h -> h번 이상 인용된 논문이 h편 이상 
        # 어차피 남은 논문이 h보다 작음
        if idx+1 > h:
            return idx
    return len(citations)