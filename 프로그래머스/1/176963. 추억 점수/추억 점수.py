def solution(name, yearning, photo):
    result = []
    for i in photo:
        answer = 0
        for j in range(len(name)):
            if name[j] in i:
                answer += yearning[j]
        result.append(answer)
    return result