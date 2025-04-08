def solution(clothes):
    # 종류별로 묶기 
    dic = {}
    for item, key in clothes:
        if key not in dic:
            dic[key] = [item]
        else:
            dic[key].append(item)
            
    answer = 1
    for i in dic.keys():
        answer *= (len(dic[i])+1)
        
    return answer-1