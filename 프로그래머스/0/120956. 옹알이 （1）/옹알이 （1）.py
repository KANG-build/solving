def solution(babbling):
    answer = 0
    for i in babbling:
        if i.replace('aya', ' ').replace('ye', ' ').replace('woo', ' ').replace('ma', ' ').strip() == '':
            print(i)
            answer += 1
    return answer