def solution(numbers):
    answer = [-1] * len(numbers)
    # 0이 빠지면 끝났다는 것
    stack = [0]
    for i in range(1, len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            # 답엔 다음에 있는 큰 수가 기록됨
            answer[stack.pop()] = numbers[i]
        # 스택에 인덱스를 기록함 (더 큰 수가 등장하지 않은)
        stack.append(i)
    return answer