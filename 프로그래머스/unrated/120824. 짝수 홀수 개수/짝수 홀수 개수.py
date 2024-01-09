def solution(num_list):
    A = 0
    B = 0
    for i in num_list:
        if i % 2 == 0:
            A += 1
        else: 
            B += 1
    answer = [A, B]
    return answer