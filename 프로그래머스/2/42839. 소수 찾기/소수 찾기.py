from itertools import permutations

def solution(numbers):
    answer = 0
    num_list = set()
    # list(numbers)로 만들 수 있는 조합 구하고
    for num in range(1, len(numbers)+1):
        for i in map(int, [''.join(i) for i in permutations(list(numbers), num)]):
            num_list.add(i)
            
    # 하나씩 소수 판별해서
    for i in num_list:
        if i in [0, 1]:
            continue
        for j in range(2, i):
            if i%j == 0:
                break
        else:
            # 되는 것들 개수 세기 
            answer += 1
            
    return answer