from collections import Counter

def solution(participant, completion):
    answer = ''
    participants = Counter(participant)
    completions = Counter(completion)
    # 완주자의 이름이 나옴
    for i in participants:
        if i in completions:
            participants[i] -= completions[i]
        if participants[i]:
            answer = i
            break
    return answer