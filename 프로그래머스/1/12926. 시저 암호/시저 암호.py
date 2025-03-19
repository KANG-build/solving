def solution(s, n):
    answer = []
    print(ord('A'), ord("Z"), ord('z'))
    for i in s:
        if i == ' ':
            answer.append(' ')
        # 대문자면 대문자에서만 민다
        elif ord('A') <= ord(i) <= ord('Z'):
            answer.append(chr(ord('A')+(ord(i)+n-ord('A'))%(ord('Z')-ord('A')+1)))
        # 소문자
        else:
            answer.append(chr(ord('a')+(ord(i)+n-ord('a'))%(ord('z')-ord('a')+1)))
    return ''.join(answer)