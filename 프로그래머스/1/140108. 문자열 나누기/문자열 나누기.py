def solution(s):
    answer = 0
    while s:
        x = s[0]
        idx, right, wrong = 0, 0, 0
        for i in range(len(s)):
            if s[i] != x:
                wrong += 1
            else: 
                right += 1
            if right == wrong:
                answer += 1
                idx = i
                break
        else:
            answer += 1
            break
        s = s[idx+1:]
    return answer