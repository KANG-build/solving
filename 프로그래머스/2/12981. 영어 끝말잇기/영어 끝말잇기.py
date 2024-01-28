def solution(n, words):
    before = [words[0]]
    for i in range(1, len(words)):
        if words[i][0] != words[i-1][-1] or words[i] in before:
            return [i%n+1, i//n+1]
        else:
            before.append(words[i])
    return [0, 0]