def solution(n, words):
    # 시작 알파벳 별로 딕셔너리 만들어서 거기서 찾으면 빠를듯?
    # 틀린 단어부터 찾고 사람을 구하자 
    set_words = set([words[0]])
    wrong_num = 0
    for i in range(1, len(words)):
        if words[i][0] != words[i-1][-1]:
            wrong_num = i
            return [wrong_num%n+1, wrong_num//n+1]
        
        if words[i] in set_words:
            wrong_num = i
            return [wrong_num%n+1, wrong_num//n+1]
        
        set_words.add(words[i])

    return [0, 0]