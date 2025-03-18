def solution(clothes):
    answer = 1
    wear_list = {}
    for a, b in clothes:
        if b in wear_list:
            wear_list[b] += 1
        else:
            wear_list[b] = 1
        
    for i in wear_list:
        answer *= (wear_list[i]+1)
        
    return answer-1