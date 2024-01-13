def solution(l, r):
    answer = []
    check = 0
    for i in range(l, r+1):
        for j in ['1', '2', '3', '4', '6', '7', '8', '9']:
            if j in str(i):
                check = 1
                
        if check == 0:
            answer.append(i)
        check = 0
        
    return answer or [-1]