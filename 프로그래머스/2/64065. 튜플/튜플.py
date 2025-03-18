def solution(s):
    # 일단 리스트로 표현한다
    num_list = []
    for i in s.split("},"):
        num_list.append(i.replace("{", "").replace("}", "").split(","))
    
    # 길이 순으로 정렬한다 
    num_list.sort(key=len)
    
    check = []
    for i in num_list:
        for num in i:
            if int(num) not in check:
                check.append(int(num))

    return check