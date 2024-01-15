def solution(food):
    answer = ''
    for idx, num in enumerate(food):
        answer += f'{idx}' * (num//2)
    return answer + '0' + answer[::-1]