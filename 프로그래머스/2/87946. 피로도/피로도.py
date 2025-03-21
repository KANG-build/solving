from itertools import combinations
from itertools import permutations

def solution(k, dungeons):
    answer = 0
    # 걍 진짜 다 해보기 
    for i in permutations(dungeons): 
        save = k
        for idx, (need, lost) in enumerate(i):  # 다 돌면 한 케이스
            if save < need:
                answer = max(answer, idx) 
                break
            save -= lost
        else:
            return len(dungeons)
    return answer