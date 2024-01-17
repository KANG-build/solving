def solution(sides):
    # 두 변의 길이의 합은 가장 긴 변의 길이보다 커야한다.
    answer = 0
    # 두 변 중 긴 변이 제일 길 경우
    for i in range(max(sides)-min(sides)+1, max(sides)):
        answer += 1
    # 더 큰 긴 변이 있을 경우
    for i in range(max(sides), sum(sides)):
        answer += 1
    return answer