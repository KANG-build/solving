def solution(n, lost, reserve):
    # reserve와 lost 겹치는 것 제거 (여벌 체육복이 도난)
    new_lost = set(lost) - set(reserve)
    new_reserve = set(reserve) - set(lost)
    
    # 내 앞사람 빌려주기 -> 뒷사람 빌려주기 순으로만 쭉 밀어도 다 해결됨 
    for i in new_reserve:
        if i-1 in new_lost:
            new_lost.remove(i-1)
        elif i+1 in new_lost:
            new_lost.remove(i+1)
    
    return n-len(new_lost)