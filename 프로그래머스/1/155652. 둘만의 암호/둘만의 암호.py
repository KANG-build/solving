def solution(s, skip, index):
    answer = []
    alp = [chr(i) for i in range(ord('a'), ord('z')+1)]
    alpha = sorted(list(set(alp) - set(skip)))
    print(alpha)
    for i in s:
        idx = (alpha.index(i) + index)%len(alpha)
        answer.append(alpha[idx])
    return ''.join(answer)