from collections import deque

def solution(numbers, target):
    leaves = [0]
    for i in numbers:
        temp = []
        
        # i번째 숫자까지 연산한 결과에 더하기, 빼기 한 경우의 수
        for leaf in leaves:
            temp.append(leaf + i)
            temp.append(leaf - i)

        # 갱신
        leaves = temp 
    
    return leaves.count(target)